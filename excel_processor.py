#!/usr/bin/env python3
"""
Excel Processor - Execute JSON commands on Excel files
Supports: set cell text, add/delete rows, apply themes, copy formats
"""

import argparse
import json
import sys
import os
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from copy import copy


class ExcelProcessor:
    def __init__(self, excel_path, debug=False, custom_presets=None):
        """Initialize the Excel processor with a workbook path."""
        self.excel_path = excel_path
        self.debug = debug
        self.workbook = None
        self.errors = []
        # Convert custom presets from JSON format to openpyxl style objects
        self.custom_presets = self._convert_presets_to_styles(custom_presets or {})
    
    def _convert_presets_to_styles(self, presets_json):
        """Convert JSON preset definitions to openpyxl style objects."""
        converted = {}
        for name, preset in presets_json.items():
            converted_preset = {}
            
            # Convert font
            if 'font' in preset:
                font_data = preset['font']
                font_kwargs = {}
                if 'name' in font_data:
                    font_kwargs['name'] = font_data['name']
                if 'size' in font_data:
                    font_kwargs['size'] = font_data['size']
                if 'bold' in font_data:
                    font_kwargs['bold'] = font_data['bold']
                if 'italic' in font_data:
                    font_kwargs['italic'] = font_data['italic']
                if 'underline' in font_data:
                    font_kwargs['underline'] = 'single' if font_data['underline'] else None
                if 'color' in font_data:
                    font_kwargs['color'] = font_data['color'].replace('#', '')
                
                if font_kwargs:
                    converted_preset['font'] = Font(**font_kwargs)
            
            # Convert fill
            if 'fill' in preset:
                fill_data = preset['fill']
                if 'color' in fill_data:
                    color = fill_data['color'].replace('#', '')
                    converted_preset['fill'] = PatternFill(
                        start_color=color,
                        end_color=color,
                        fill_type='solid'
                    )
            
            # Convert alignment
            if 'alignment' in preset:
                align_data = preset['alignment']
                align_kwargs = {}
                if 'horizontal' in align_data:
                    align_kwargs['horizontal'] = align_data['horizontal']
                if 'vertical' in align_data:
                    align_kwargs['vertical'] = align_data['vertical']
                if 'wrap_text' in align_data:
                    align_kwargs['wrap_text'] = align_data['wrap_text']
                
                if align_kwargs:
                    converted_preset['alignment'] = Alignment(**align_kwargs)
            
            converted[name] = converted_preset
        
        return converted
        
    def load_workbook(self):
        """Load the Excel workbook."""
        try:
            self.workbook = load_workbook(self.excel_path)
            if self.debug:
                print(f"✓ Loaded workbook: {self.excel_path}")
            return True
        except Exception as e:
            error_msg = f"Failed to load workbook: {str(e)}"
            self.errors.append(error_msg)
            if self.debug:
                print(f"✗ {error_msg}")
            return False
    
    def save_workbook(self, output_path=None):
        """Save the workbook to the specified path or overwrite the original."""
        try:
            save_path = output_path if output_path else self.excel_path
            self.workbook.save(save_path)
            if self.debug:
                print(f"✓ Saved workbook to: {save_path}")
            return True
        except Exception as e:
            error_msg = f"Failed to save workbook: {str(e)}"
            self.errors.append(error_msg)
            if self.debug:
                print(f"✗ {error_msg}")
            return False
    
    def execute_commands(self, commands):
        """Execute a list of commands from JSON."""
        for idx, command in enumerate(commands):
            cmd_type = command.get('command')
            if self.debug:
                print(f"\nExecuting command {idx + 1}: {cmd_type}")
            
            try:
                if cmd_type == 'set_cell_text':
                    self._set_cell_text(command)
                elif cmd_type == 'add_row':
                    self._add_row(command)
                elif cmd_type == 'delete_row':
                    self._delete_row(command)
                elif cmd_type == 'set_theme':
                    self._set_theme(command)
                elif cmd_type == 'copy_format':
                    self._copy_format(command)
                else:
                    error_msg = f"Unknown command: {cmd_type}"
                    self.errors.append(error_msg)
                    if self.debug:
                        print(f"✗ {error_msg}")
            except Exception as e:
                error_msg = f"Error executing command {idx + 1} ({cmd_type}): {str(e)}"
                self.errors.append(error_msg)
                if self.debug:
                    print(f"✗ {error_msg}")
    
    def _set_cell_text(self, command):
        """Set text in a specific cell."""
        sheet_name = command.get('sheet')
        row = command.get('row')
        column = command.get('column')
        text = command.get('text', '')
        
        if sheet_name not in self.workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' not found")
        
        sheet = self.workbook[sheet_name]
        cell = sheet.cell(row=row, column=column)
        cell.value = text
        
        if self.debug:
            print(f"  ✓ Set cell [{sheet_name}!{get_column_letter(column)}{row}] = '{text}'")
    
    def _add_row(self, command):
        """Add a row after the specified row number."""
        sheet_name = command.get('sheet')
        after_row = command.get('after_row')
        
        if sheet_name not in self.workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' not found")
        
        sheet = self.workbook[sheet_name]
        sheet.insert_rows(after_row + 1)
        
        if self.debug:
            print(f"  ✓ Added row after row {after_row} in sheet '{sheet_name}'")
    
    def _delete_row(self, command):
        """Delete a specific row."""
        sheet_name = command.get('sheet')
        row_number = command.get('row')
        
        if sheet_name not in self.workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' not found")
        
        sheet = self.workbook[sheet_name]
        sheet.delete_rows(row_number)
        
        if self.debug:
            print(f"  ✓ Deleted row {row_number} in sheet '{sheet_name}'")
    
    def _set_theme(self, command):
        """Apply theme/styling to a cell."""
        sheet_name = command.get('sheet')
        row = command.get('row')
        column = command.get('column')
        theme = command.get('theme')
        
        if sheet_name not in self.workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' not found")
        
        sheet = self.workbook[sheet_name]
        cell = sheet.cell(row=row, column=column)
        
        # Check if using preset or custom theme
        if isinstance(theme, str):
            # Preset theme
            self._apply_preset_theme(cell, theme)
        elif isinstance(theme, dict):
            # Custom theme
            self._apply_custom_theme(cell, theme)
        else:
            raise ValueError(f"Invalid theme format: {theme}")
        
        if self.debug:
            theme_desc = theme if isinstance(theme, str) else "custom"
            print(f"  ✓ Applied theme '{theme_desc}' to cell [{sheet_name}!{get_column_letter(column)}{row}]")
    
    def _apply_preset_theme(self, cell, preset_name):
        """Apply a preset theme to a cell."""
        builtin_presets = {
            'header': {
                'font': Font(name='Arial', size=12, bold=True, color='FFFFFF'),
                'fill': PatternFill(start_color='366092', end_color='366092', fill_type='solid'),
                'alignment': Alignment(horizontal='center', vertical='center')
            },
            'title': {
                'font': Font(name='Arial', size=14, bold=True, color='000000'),
                'fill': PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid'),
                'alignment': Alignment(horizontal='center', vertical='center')
            },
            'highlight': {
                'font': Font(name='Arial', size=11, bold=False, color='000000'),
                'fill': PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid'),
                'alignment': Alignment(horizontal='left', vertical='center')
            },
            'warning': {
                'font': Font(name='Arial', size=11, bold=True, color='FFFFFF'),
                'fill': PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid'),
                'alignment': Alignment(horizontal='center', vertical='center')
            },
            'success': {
                'font': Font(name='Arial', size=11, bold=False, color='FFFFFF'),
                'fill': PatternFill(start_color='00B050', end_color='00B050', fill_type='solid'),
                'alignment': Alignment(horizontal='center', vertical='center')
            },
            'default': {
                'font': Font(name='Arial', size=11, bold=False, color='000000'),
                'fill': PatternFill(fill_type=None),
                'alignment': Alignment(horizontal='left', vertical='center')
            }
        }
        
        # Merge built-in and custom presets (custom presets override built-in)
        presets = {**builtin_presets, **self.custom_presets}
        
        if preset_name not in presets:
            available = list(builtin_presets.keys())
            custom_list = list(self.custom_presets.keys())
            error_msg = f"Unknown preset theme: {preset_name}. Built-in: {', '.join(available)}"
            if custom_list:
                error_msg += f". Custom: {', '.join(custom_list)}"
            raise ValueError(error_msg)
        
        theme = presets[preset_name]
        if 'font' in theme:
            cell.font = theme['font']
        if 'fill' in theme:
            cell.fill = theme['fill']
        if 'alignment' in theme:
            cell.alignment = theme['alignment']
    
    def _apply_custom_theme(self, cell, theme_data):
        """Apply custom styling to a cell."""
        # Apply font settings
        if 'font' in theme_data or any(k in theme_data for k in ['font_name', 'font_size', 'bold', 'italic', 'underline', 'font_color']):
            font_kwargs = {}
            
            if 'font_name' in theme_data:
                font_kwargs['name'] = theme_data['font_name']
            if 'font_size' in theme_data:
                font_kwargs['size'] = theme_data['font_size']
            if 'bold' in theme_data:
                font_kwargs['bold'] = theme_data['bold']
            if 'italic' in theme_data:
                font_kwargs['italic'] = theme_data['italic']
            if 'underline' in theme_data:
                font_kwargs['underline'] = 'single' if theme_data['underline'] else None
            if 'font_color' in theme_data:
                font_kwargs['color'] = theme_data['font_color'].replace('#', '')
            
            if font_kwargs:
                cell.font = Font(**font_kwargs)
        
        # Apply fill/background color
        if 'bg_color' in theme_data or 'background_color' in theme_data:
            bg_color = theme_data.get('bg_color') or theme_data.get('background_color')
            bg_color = bg_color.replace('#', '')
            cell.fill = PatternFill(start_color=bg_color, end_color=bg_color, fill_type='solid')
        
        # Apply alignment
        if any(k in theme_data for k in ['horizontal', 'vertical', 'wrap_text']):
            align_kwargs = {}
            
            if 'horizontal' in theme_data:
                align_kwargs['horizontal'] = theme_data['horizontal']
            if 'vertical' in theme_data:
                align_kwargs['vertical'] = theme_data['vertical']
            if 'wrap_text' in theme_data:
                align_kwargs['wrap_text'] = theme_data['wrap_text']
            
            if align_kwargs:
                cell.alignment = Alignment(**align_kwargs)
        
        # Apply borders
        if 'border' in theme_data:
            border_data = theme_data['border']
            border_style = border_data.get('style', 'thin')
            border_color = border_data.get('color', '000000').replace('#', '')
            
            side = Side(style=border_style, color=border_color)
            
            border_kwargs = {
                'left': side if border_data.get('left', True) else None,
                'right': side if border_data.get('right', True) else None,
                'top': side if border_data.get('top', True) else None,
                'bottom': side if border_data.get('bottom', True) else None,
            }
            
            cell.border = Border(**border_kwargs)
    
    def _copy_format(self, command):
        """Copy formatting from one cell to another."""
        source_sheet = command.get('source_sheet')
        source_row = command.get('source_row')
        source_column = command.get('source_column')
        
        target_sheet = command.get('target_sheet')
        target_row = command.get('target_row')
        target_column = command.get('target_column')
        
        if source_sheet not in self.workbook.sheetnames:
            raise ValueError(f"Source sheet '{source_sheet}' not found")
        if target_sheet not in self.workbook.sheetnames:
            raise ValueError(f"Target sheet '{target_sheet}' not found")
        
        source_cell = self.workbook[source_sheet].cell(row=source_row, column=source_column)
        target_cell = self.workbook[target_sheet].cell(row=target_row, column=target_column)
        
        # Copy all formatting attributes
        if source_cell.has_style:
            target_cell.font = copy(source_cell.font)
            target_cell.fill = copy(source_cell.fill)
            target_cell.border = copy(source_cell.border)
            target_cell.alignment = copy(source_cell.alignment)
            target_cell.number_format = copy(source_cell.number_format)
            target_cell.protection = copy(source_cell.protection)
        
        if self.debug:
            print(f"  ✓ Copied format from [{source_sheet}!{get_column_letter(source_column)}{source_row}] "
                  f"to [{target_sheet}!{get_column_letter(target_column)}{target_row}]")
    
    def has_errors(self):
        """Check if any errors occurred during processing."""
        return len(self.errors) > 0
    
    def get_error_summary(self):
        """Get a summary of all errors."""
        return "\n".join(self.errors)


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
        description='Execute JSON commands on Excel files. Commands are executed sequentially, '
                    'errors are collected and reported at the end. Status file is always created.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process commands and overwrite original file
  %(prog)s input.xlsx commands.json
  
  # Process commands and save to new file
  %(prog)s input.xlsx commands.json -o output.xlsx
  
  # Enable debug output and custom status file
  %(prog)s input.xlsx commands.json --debug --status-file status.txt
  
  # Use custom theme presets
  %(prog)s input.xlsx commands.json --presets my_themes.json

JSON Format:
  The JSON file must contain an array of command objects. Each command
  must have a "command" field specifying the operation type.
  
  Supported commands: set_cell_text, add_row, delete_row, set_theme, copy_format

Behavior:
  - Commands are executed in order from the JSON array
  - If errors occur, remaining commands still execute
  - All errors are collected and reported at the end
  - Status file is always created (0 = success, 1 = failure with details)
  - Exit code 0 for success, 1 for any errors
        """
    )
    
    parser.add_argument('excel_file', help='Path to the Excel file to process')
    parser.add_argument('json_file', help='Path to the JSON file containing an array of commands')
    parser.add_argument('-o', '--output', help='Output Excel file path (default: overwrite input file)')
    parser.add_argument('--presets', help='Path to JSON file with custom theme presets (optional)')
    parser.add_argument('--status-file', help='Status file path (default: <excel_file_dir>/status.txt). Always created.')
    parser.add_argument('--debug', action='store_true', help='Enable debug output with detailed execution info')
    
    args = parser.parse_args()
    
    # Validate input files exist
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
        # Load custom presets if provided
        custom_presets = {}
        if args.presets:
            if not os.path.exists(args.presets):
                print(f"Error: Presets file not found: {args.presets}", file=sys.stderr)
                sys.exit(1)
            
            try:
                with open(args.presets, 'r', encoding='utf-8') as f:
                    custom_presets = json.load(f)
                
                if args.debug:
                    print(f"Loaded {len(custom_presets)} custom theme presets from {args.presets}")
            except json.JSONDecodeError as e:
                error_msg = f"Invalid presets JSON file: {str(e)}"
                print(f"Error: {error_msg}", file=sys.stderr)
                write_status_file(status_path, False, error_msg)
                sys.exit(1)
        
        # Load JSON commands
        with open(args.json_file, 'r', encoding='utf-8') as f:
            commands = json.load(f)
        
        if args.debug:
            print(f"Loaded {len(commands)} commands from {args.json_file}")
        
        # Process Excel file
        processor = ExcelProcessor(args.excel_file, debug=args.debug, custom_presets=custom_presets)
        
        if not processor.load_workbook():
            write_status_file(status_path, False, processor.get_error_summary())
            sys.exit(1)
        
        processor.execute_commands(commands)
        
        if processor.has_errors():
            error_summary = processor.get_error_summary()
            print(f"\nErrors occurred during processing:\n{error_summary}", file=sys.stderr)
            write_status_file(status_path, False, error_summary)
            sys.exit(1)
        
        if not processor.save_workbook(args.output):
            write_status_file(status_path, False, processor.get_error_summary())
            sys.exit(1)
        
        # Success
        write_status_file(status_path, True)
        
        if args.debug:
            print(f"\n✓ All commands executed successfully")
            print(f"✓ Status file written to: {status_path}")
        
        sys.exit(0)
        
    except json.JSONDecodeError as e:
        error_msg = f"Invalid JSON file: {str(e)}"
        print(f"Error: {error_msg}", file=sys.stderr)
        write_status_file(status_path, False, error_msg)
        sys.exit(1)
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(f"Error: {error_msg}", file=sys.stderr)
        write_status_file(status_path, False, error_msg)
        sys.exit(1)


if __name__ == '__main__':
    main()
