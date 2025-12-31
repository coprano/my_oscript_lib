#!/usr/bin/env python3
"""
Excel XML Editor - Modify Excel files by editing XML directly
Preserves all images, drawings, charts, and formatting
"""

import zipfile
import xml.etree.ElementTree as ET
import tempfile
import shutil
import os
import json
import argparse
import sys
import re


# Excel namespace
EXCEL_NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'


def column_letter_to_number(column_letter):
    """Convert 'A' -> 1, 'B' -> 2, 'AA' -> 27, etc."""
    num = 0
    for char in column_letter.upper():
        num = num * 26 + (ord(char) - ord('A') + 1)
    return num


def number_to_column_letter(num):
    """Convert 1 -> 'A', 2 -> 'B', 27 -> 'AA', etc."""
    letter = ''
    while num > 0:
        num -= 1
        letter = chr(num % 26 + ord('A')) + letter
        num //= 26
    return letter


def normalize_column(column):
    """Convert column to integer. Accepts both int (1, 2, 3) and string ('A', 'B', 'C')."""
    if isinstance(column, int):
        return column
    elif isinstance(column, str):
        try:
            return column_letter_to_number(column.upper())
        except Exception:
            raise ValueError(f"Invalid column identifier: '{column}'")
    else:
        raise ValueError(f"Column must be int or str, got {type(column)}")


def cell_ref_to_row_col(cell_ref):
    """Convert 'A1' to (1, 1), 'B2' to (2, 2), etc."""
    match = re.match(r'([A-Z]+)(\d+)', cell_ref.upper())
    if not match:
        raise ValueError(f"Invalid cell reference: {cell_ref}")
    col = column_letter_to_number(match.group(1))
    row = int(match.group(2))
    return (row, col)


def row_col_to_cell_ref(row, col):
    """Convert (1, 1) to 'A1', (2, 2) to 'B2', etc."""
    return f"{number_to_column_letter(col)}{row}"


def modify_worksheet_xml(xml_data, commands, sheet_name, debug=False):
    """
    Parse worksheet XML, apply commands, and return modified XML.
    Uses text-based manipulation to preserve exact structure and namespaces.
    """
    try:
        # Convert to string
        xml_str = xml_data.decode('utf-8') if isinstance(xml_data, bytes) else xml_data
        
        # Apply commands for this sheet
        for cmd in commands:
            if cmd.get('sheet') != sheet_name:
                continue
            
            if cmd.get('command') == 'set_cell_value':
                row = cmd.get('row')
                col = normalize_column(cmd.get('column'))
                value = cmd.get('text', '')
                xml_str = set_cell_value_text(xml_str, row, col, value, debug)
        
        return xml_str.encode('utf-8')
    
    except Exception as e:
        if debug:
            print(f"  Error modifying worksheet: {e}")
            import traceback
            traceback.print_exc()
        return xml_data


def set_cell_value_text(xml_str, row, col, value, debug=False):
    """
    Set cell value using simple text replacement - very conservative approach.
    """
    cell_ref = row_col_to_cell_ref(row, col)
    value_str = str(value) if value else ""
    
    # Detect if value is a number (but only for non-empty values)
    is_number = False
    if value_str:
        try:
            float(value_str)
            is_number = True
        except ValueError:
            is_number = False
    
    # Escape XML special characters (backslash doesn't need escaping in XML)
    escaped_value = (value_str
                    .replace('&', '&amp;')
                    .replace('<', '&lt;')
                    .replace('>', '&gt;')
                    .replace('"', '&quot;')
                    .replace("'", '&apos;')
                    .replace('\n', '&#10;')
                    .replace('\r', '&#13;')
                    .replace('\t', '&#9;'))
    
    # Find the cell element - match exact cell reference only
    # Try self-closing tag first, then regular tag
    cell_pattern_selfclosing = rf'<c r="{re.escape(cell_ref)}"[^/>]*/>'
    cell_match = re.search(cell_pattern_selfclosing, xml_str)
    
    if not cell_match:
        # Try regular tag with content
        cell_pattern = rf'<c r="{re.escape(cell_ref)}"[^>]*>.*?</c>'
        cell_match = re.search(cell_pattern, xml_str, re.DOTALL)
    
    if cell_match:
        # Cell exists - replace ONLY the content between tags
        old_cell = cell_match.group(0)
        
        # Check if it's a self-closing tag
        is_self_closing = old_cell.strip().endswith('/>')
        
        if is_self_closing:
            # Handle self-closing tag like <c r="C16" s="15"/>
            # Extract the opening part without the />
            opening_part = old_cell[:old_cell.rfind('/>')]
            # Remove type attribute if present
            opening_part = re.sub(r'\s+t="[^"]*"', '', opening_part)
            # Remove self-closing slash if present
            opening_part = opening_part.rstrip().rstrip('/')
        else:
            # Regular tag with content
            # Find the content between <c...> and </c>
            content_start = old_cell.find('>') + 1
            content_end = old_cell.rfind('</')
            
            if content_start <= 0 or content_end <= 0 or content_end <= content_start:
                if debug:
                    print(f"  ⚠ Could not parse cell content for {cell_ref}")
                return xml_str
            
            # Extract opening tag and preserve all attributes except 't'
            opening_part = old_cell[:content_start]
            # Remove type attribute and add our own, but be very careful
            opening_part = re.sub(r'\s+t="[^"]*"', '', opening_part)
            # Remove the trailing >
            if opening_part.endswith('>'):
                opening_part = opening_part[:-1]
        
        # Build new cell content
        if is_number and value_str:
            new_type = ' t="n"'
            new_content = f'<v>{value_str}</v>'
        elif value_str:
            new_type = ' t="inlineStr"'
            new_content = f'<is><t>{escaped_value}</t></is>'
        else:
            new_type = ''
            new_content = ''
        
        # Build the new cell
        new_cell = opening_part + new_type + '>' + new_content + '</c>'
        xml_str = xml_str.replace(old_cell, new_cell, 1)
        
        if debug:
            print(f"  ✓ Set cell {cell_ref} = '{value_str}'")
    else:
        # Cell doesn't exist - add it using simple insertion
        xml_str = insert_new_cell_simple(xml_str, row, col, value_str, is_number, escaped_value, debug)
    
    return xml_str


def insert_new_cell_simple(xml_str, row, col, value_str, is_number, escaped_value, debug=False):
    """
    Ultra-safe cell insertion that preserves XML structure completely.
    """
    cell_ref = row_col_to_cell_ref(row, col)
    
    # Build the new cell element - be very explicit about structure
    if is_number and value_str:
        cell_xml = f'<c r="{cell_ref}" t="n"><v>{value_str}</v></c>'
    elif value_str:
        cell_xml = f'<c r="{cell_ref}" t="inlineStr"><is><t>{escaped_value}</t></is></c>'
    else:
        # Empty cell - no type attribute, no content
        cell_xml = f'<c r="{cell_ref}"></c>'
    
    # Look for existing row - handle both regular and self-closing rows
    # Try self-closing first
    row_pattern_selfclosing = rf'<row r="{row}"[^/>]*/>'  
    row_match = re.search(row_pattern_selfclosing, xml_str)
    
    if not row_match:
        # Try regular row with content
        row_pattern = rf'<row r="{row}"([^>]*)>(.*?)</row>'
        row_match = re.search(row_pattern, xml_str, re.DOTALL)
    
    if row_match:
        # Row exists - insert cell in correct column order
        old_row_full = row_match.group(0)
        
        # Check if it's a self-closing row
        is_selfclosing_row = old_row_full.strip().endswith('/>')
        
        if is_selfclosing_row:
            # Convert self-closing row to regular row with content
            # Extract attributes from self-closing tag
            row_opening = old_row_full[:old_row_full.rfind('/>')]
            row_attrs = row_opening[row_opening.find(f'r="{row}"')+len(f'r="{row}"'):]
            row_content = ''
        else:
            # Regular row with content
            row_attrs = row_match.group(1)
            row_content = row_match.group(2)
        
        # Find all existing cells in this row and their column positions
        existing_cells = list(re.finditer(r'<c r="([A-Z]+)\d+"[^>]*(?:>.*?</c>|/>)', row_content, re.DOTALL))
        
        inserted = False
        if existing_cells:
            # Find the correct position to insert based on column order
            for cell_match in existing_cells:
                existing_col_letter = cell_match.group(1)
                existing_col_num = column_letter_to_number(existing_col_letter)
                
                if col > existing_col_num:
                    # Continue looking
                    continue
                else:
                    # Insert before this cell
                    pos = cell_match.start()
                    new_content = row_content[:pos] + cell_xml + row_content[pos:]
                    new_row = f'<row r="{row}"{row_attrs}>{new_content}</row>'
                    xml_str = xml_str.replace(old_row_full, new_row, 1)
                    inserted = True
                    break
            
            if not inserted:
                # Append at the end (column is after all existing cells)
                new_row = f'<row r="{row}"{row_attrs}>{row_content}{cell_xml}</row>'
                xml_str = xml_str.replace(old_row_full, new_row, 1)
        else:
            # No existing cells, just add it
            new_row = f'<row r="{row}"{row_attrs}>{cell_xml}</row>'
            xml_str = xml_str.replace(old_row_full, new_row, 1)
        
        if debug:
            print(f"  ✓ Set cell {cell_ref} = '{value_str}'")
    else:
        # Row doesn't exist - create minimal row and insert in correct order
        row_xml = f'<row r="{row}">{cell_xml}</row>'
        
        # Find sheetData and insert row in correct position
        sheetdata_pattern = r'(<sheetData>)(.*?)(</sheetData>)'
        sheetdata_match = re.search(sheetdata_pattern, xml_str, re.DOTALL)
        
        if sheetdata_match:
            sheetdata_open = sheetdata_match.group(1)
            sheetdata_content = sheetdata_match.group(2)
            sheetdata_close = sheetdata_match.group(3)
            old_sheetdata_full = sheetdata_match.group(0)
            
            # Find all existing rows and their positions (including self-closing)
            existing_rows = list(re.finditer(r'<row r="(\d+)"[^>]*(?:>.*?</row>|/>)', sheetdata_content, re.DOTALL))
            
            inserted = False
            if existing_rows:
                # Find the correct position to insert
                for i, row_match in enumerate(existing_rows):
                    existing_row_num = int(row_match.group(1))
                    if row > existing_row_num:
                        # Continue looking
                        continue
                    else:
                        # Insert before this row
                        pos = row_match.start()
                        new_content = sheetdata_content[:pos] + row_xml + sheetdata_content[pos:]
                        new_sheetdata = sheetdata_open + new_content + sheetdata_close
                        xml_str = xml_str.replace(old_sheetdata_full, new_sheetdata, 1)
                        inserted = True
                        break
                
                if not inserted:
                    # Insert at the end (row number is larger than all existing)
                    new_sheetdata = sheetdata_open + sheetdata_content + row_xml + sheetdata_close
                    xml_str = xml_str.replace(old_sheetdata_full, new_sheetdata, 1)
            else:
                # No existing rows, just add it
                new_sheetdata = sheetdata_open + row_xml + sheetdata_close
                xml_str = xml_str.replace(old_sheetdata_full, new_sheetdata, 1)
            
            if debug:
                print(f"  Created row {row}")
                print(f"  ✓ Set cell {cell_ref} = '{value_str}'")
        else:
            if debug:
                print(f"  ⚠ Could not find sheetData element")
    
    return xml_str


def get_sheet_name_from_path(sheet_path, workbook_xml, rels_xml):
    """
    Extract sheet name from sheet path using workbook.xml and workbook.xml.rels.
    """
    # Extract sheet number from path (e.g., 'xl/worksheets/sheet1.xml' -> '1')
    match = re.search(r'sheet(\d+)\.xml', sheet_path)
    if not match:
        return None
    
    sheet_num = match.group(1)
    
    # Parse workbook.xml to find sheet name
    try:
        ET.register_namespace('', EXCEL_NS)
        root = ET.fromstring(workbook_xml)
        
        # Find sheets element
        for elem in root:
            tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
            if tag == 'sheets':
                # Find sheet with matching rId
                for sheet in elem:
                    sheet_id = sheet.get('sheetId', '')
                    if sheet_id == sheet_num:
                        return sheet.get('name', f'Sheet{sheet_num}')
                    # Also try matching by rId
                    r_id = sheet.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id', '')
                    if r_id:
                        # Parse rels to match rId to target
                        # For simplicity, use sheetId match for now
                        pass
        
        # Fallback: use sheet order
        sheet_index = int(sheet_num) - 1
        for i, elem in enumerate(root.iter(f'{{{EXCEL_NS}}}sheet')):
            if i == sheet_index:
                return elem.get('name', f'Sheet{sheet_num}')
    except:
        pass
    
    return f'Sheet{sheet_num}'


def modify_excel_file(input_path, output_path, commands, debug=False):
    """
    Main function: Opens Excel ZIP, modifies worksheet XMLs, preserves everything else.
    """
    if not os.path.exists(input_path):
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        return False
    
    # Build a map of sheet paths to sheet names
    sheet_map = {}
    workbook_xml = None
    rels_xml = None
    
    try:
        with zipfile.ZipFile(input_path, 'r') as src_zip:
            # Read workbook.xml to get sheet names
            if 'xl/workbook.xml' in src_zip.namelist():
                workbook_xml = src_zip.read('xl/workbook.xml')
            if 'xl/_rels/workbook.xml.rels' in src_zip.namelist():
                rels_xml = src_zip.read('xl/_rels/workbook.xml.rels')
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        return False
    
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_output = os.path.join(tmpdir, 'output.xlsx')
        
        try:
            with zipfile.ZipFile(input_path, 'r') as src_zip:
                with zipfile.ZipFile(temp_output, 'w', zipfile.ZIP_DEFLATED) as dst_zip:
                    # Copy all files, modifying worksheets as needed
                    for item in src_zip.namelist():
                        # Skip calcChain.xml - Excel will regenerate it
                        # This prevents "removed formula" errors when cells are modified
                        if item == 'xl/calcChain.xml':
                            if debug:
                                print(f"\nSkipping {item} (will be regenerated by Excel)")
                            continue
                        
                        data = src_zip.read(item)
                        
                        # Check if this is a worksheet XML
                        if item.startswith('xl/worksheets/sheet') and item.endswith('.xml'):
                            # Get sheet name
                            sheet_name = get_sheet_name_from_path(item, workbook_xml, rels_xml)
                            
                            if debug:
                                print(f"\nProcessing {item} (sheet: {sheet_name})")
                            
                            # Modify worksheet XML
                            data = modify_worksheet_xml(data, commands, sheet_name, debug)
                        
                        # Write to output ZIP
                        dst_zip.writestr(item, data)
            
            # Move temp file to output path
            shutil.move(temp_output, output_path)
            return True
        
        except Exception as e:
            print(f"Error processing Excel file: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            return False


def write_status_file(status_path, success, error_message=""):
    """Write status file with success/failure information."""
    try:
        with open(status_path, 'w') as f:
            if success:
                f.write("0")
            else:
                f.write(f"1\n{error_message}")
        return True
    except Exception as e:
        print(f"Warning: Failed to write status file: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Execute JSON commands on Excel files using direct XML editing. '
                    'Preserves all images, drawings, charts, and formatting.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Modify cells and save to new file
  %(prog)s --excel-file input.xlsx --json-file commands.json -o output.xlsx
  
  # Enable debug output
  %(prog)s --excel-file input.xlsx --json-file commands.json -o output.xlsx --debug

JSON Command Format:
  [
    {
      "command": "set_cell_value",
      "sheet": "Sheet1",
      "row": 1,
      "column": "A",
      "text": "Hello World"
    }
  ]

Supported Commands:
  - set_cell_value: Set text/number in a cell
    - sheet: Sheet name (e.g., "Sheet1")
    - row: Row number (1-based)
    - column: Column letter or number (e.g., "A" or 1)
    - text: Value to set
        """
    )
    
    parser.add_argument('--excel-file', required=True, help='Path to input Excel file')
    parser.add_argument('--json-file', required=True, help='Path to JSON commands file')
    parser.add_argument('-o', '--output-file', required=True, help='Path to output Excel file')
    parser.add_argument('--status-file', help='Status file path (default: <excel_file_dir>/status.txt)')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    
    args = parser.parse_args()
    
    # Validate input files
    if not os.path.exists(args.excel_file):
        print(f"Error: Excel file not found: {args.excel_file}", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.exists(args.json_file):
        print(f"Error: JSON file not found: {args.json_file}", file=sys.stderr)
        sys.exit(1)
    
    # Determine status file path
    if args.status_file:
        status_path = args.status_file
    else:
        excel_dir = os.path.dirname(os.path.abspath(args.excel_file))
        status_path = os.path.join(excel_dir, 'status.txt')
    
    try:
        # Load JSON commands
        with open(args.json_file, 'r', encoding='utf-8') as f:
            commands = json.load(f)
        
        if args.debug:
            print(f"Loaded {len(commands)} commands from {args.json_file}")
        
        # Process Excel file
        success = modify_excel_file(args.excel_file, args.output_file, commands, args.debug)
        
        if success:
            write_status_file(status_path, True)
            if args.debug:
                print(f"\n✓ Successfully created {args.output_file}")
                print(f"✓ Status file written to: {status_path}")
            sys.exit(0)
        else:
            write_status_file(status_path, False, "Failed to process Excel file")
            sys.exit(1)
    
    except json.JSONDecodeError as e:
        error_msg = f"Invalid JSON file: {str(e)}"
        print(f"Error: {error_msg}", file=sys.stderr)
        write_status_file(status_path, False, error_msg)
        sys.exit(1)
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(f"Error: {error_msg}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        write_status_file(status_path, False, error_msg)
        sys.exit(1)


if __name__ == '__main__':
    main()
