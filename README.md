# Excel Processor

A Python script that executes JSON commands to manipulate Excel files.

## Features

- **Set Cell Text**: Write text to specific cells
- **Add/Delete Rows**: Insert or remove rows dynamically
- **Apply Themes**: Use preset themes or custom styling
- **Copy Formats**: Copy cell formatting between cells
- **Status Tracking**: Automatic status file generation
- **Debug Mode**: Detailed execution logging

## Installation

```bash
pip install openpyxl
```

## Usage

### Basic Usage

```bash
# Overwrite original file
python excel_processor.py input.xlsx commands.json

# Save to new file
python excel_processor.py input.xlsx commands.json -o output.xlsx

# Enable debug output
python excel_processor.py input.xlsx commands.json --debug

# Custom status file location
python excel_processor.py input.xlsx commands.json --status-file /path/to/status.txt

# Use custom theme presets
python excel_processor.py input.xlsx commands.json --presets my_themes.json
```

### Command Line Arguments

- `excel_file`: Path to the Excel file to process (required)
- `json_file`: Path to the JSON file containing an array of commands (required)
- `-o, --output`: Output Excel file path (default: overwrite input file)
- `--presets`: Path to JSON file with custom theme presets (optional)
- `--status-file`: Path to status file (default: status.txt in Excel file directory). Status file is **always created**.
- `--debug`: Enable debug output showing detailed execution information

### JSON File Format

The JSON file must contain an **array** of command objects:

```json
[
  {
    "command": "set_cell_text",
    "sheet": "Sheet1",
    "row": 1,
    "column": 1,
    "text": "Hello"
  },
  {
    "command": "set_theme",
    "sheet": "Sheet1",
    "row": 1,
    "column": 1,
    "theme": "header"
  }
]
```

### Execution Behavior

**Important execution characteristics:**

- Commands are executed **sequentially** in the order they appear in the JSON array
- If a command fails, the script **continues executing** remaining commands
- All errors are **collected** and reported together at the end
- Status file is **always created** (even on success)
- The script validates that input files exist before processing
- Sheet names are validated - errors are reported if sheets don't exist

## JSON Command Format

All commands are placed in a JSON array. Each command object must have a `"command"` field.

### Set Cell Text

Sets the value of a specific cell.

**Parameters:**
- `sheet` (string): Sheet name
- `row` (integer): Row number (1-indexed)
- `column` (integer): Column number (1-indexed)
- `text` (string): Text to set (optional, defaults to empty string)

```json
{
  "command": "set_cell_text",
  "sheet": "Sheet1",
  "row": 1,
  "column": 1,
  "text": "Hello World"
}
```

### Add Row

Inserts a new blank row after the specified row number.

**Parameters:**
- `sheet` (string): Sheet name
- `after_row` (integer): Insert new row after this row number

```json
{
  "command": "add_row",
  "sheet": "Sheet1",
  "after_row": 5
}
```

### Delete Row

Deletes the specified row and shifts remaining rows up.

**Parameters:**
- `sheet` (string): Sheet name
- `row` (integer): Row number to delete

```json
{
  "command": "delete_row",
  "sheet": "Sheet1",
  "row": 3
}
```

### Set Theme (Preset)

Applies a predefined style to a cell.

**Parameters:**
- `sheet` (string): Sheet name
- `row` (integer): Row number
- `column` (integer): Column number
- `theme` (string): Preset name

**Available presets:** `header`, `title`, `highlight`, `warning`, `success`, `default`

```json
{
  "command": "set_theme",
  "sheet": "Sheet1",
  "row": 1,
  "column": 1,
  "theme": "header"
}
```

### Set Theme (Custom)

Applies custom formatting to a cell. All properties are optional.

**Parameters:**
- `sheet` (string): Sheet name
- `row` (integer): Row number
- `column` (integer): Column number
- `theme` (object): Custom theme properties (see Custom Theme Properties section)

```json
{
  "command": "set_theme",
  "sheet": "Sheet1",
  "row": 2,
  "column": 1,
  "theme": {
    "font_name": "Arial",
    "font_size": 12,
    "bold": true,
    "italic": false,
    "underline": false,
    "font_color": "#FF0000",
    "bg_color": "#FFFF00",
    "horizontal": "center",
    "vertical": "center",
    "wrap_text": false,
    "border": {
      "style": "thin",
      "color": "#000000",
      "left": true,
      "right": true,
      "top": true,
      "bottom": true
    }
  }
}
```

### Copy Format

Copies all formatting (font, colors, borders, alignment, etc.) from one cell to another. Does not copy the cell value.

**Parameters:**
- `source_sheet` (string): Source sheet name
- `source_row` (integer): Source row number
- `source_column` (integer): Source column number
- `target_sheet` (string): Target sheet name
- `target_row` (integer): Target row number
- `target_column` (integer): Target column number

```json
{
  "command": "copy_format",
  "source_sheet": "Sheet1",
  "source_row": 1,
  "source_column": 1,
  "target_sheet": "Sheet1",
  "target_row": 5,
  "target_column": 1
}
```

## Custom Theme Properties

### Font Properties
- `font_name`: Font family name (e.g., "Arial", "Calibri")
- `font_size`: Font size in points (e.g., 11, 12, 14)
- `bold`: Boolean for bold text
- `italic`: Boolean for italic text
- `underline`: Boolean for underlined text
- `font_color`: Hex color code (e.g., "#FF0000" or "FF0000") - `#` is optional

### Background
- `bg_color` or `background_color`: Hex color code for cell background - `#` is optional

### Alignment
- `horizontal`: "left", "center", "right", "justify"
- `vertical`: "top", "center", "bottom"
- `wrap_text`: Boolean for text wrapping

### Border
- `border.style`: "thin", "medium", "thick", "double", "dotted", "dashed"
- `border.color`: Hex color code - `#` is optional
- `border.left`, `border.right`, `border.top`, `border.bottom`: Boolean for each side (default: true)

## Preset Themes

### Built-in Presets

The script includes the following built-in themes:

#### Header
- Bold white text on blue background
- Center aligned

#### Title
- Bold black text on light blue background
- Center aligned

#### Highlight
- Regular text on yellow background
- Left aligned

#### Warning
- Bold white text on red background
- Center aligned

#### Success
- White text on green background
- Center aligned

#### Default
- Regular black text
- No background
- Left aligned

### Custom Presets

You can define your own theme presets in a separate JSON file and load them with the `--presets` argument.

**Custom presets file format (`my_themes.json`):**
```json
{
  "company_header": {
    "font": {
      "name": "Calibri",
      "size": 14,
      "bold": true,
      "color": "#FFFFFF"
    },
    "fill": {
      "color": "#002060"
    },
    "alignment": {
      "horizontal": "center",
      "vertical": "center"
    }
  },
  "subtotal": {
    "font": {
      "name": "Arial",
      "size": 11,
      "bold": true,
      "color": "#000000"
    },
    "fill": {
      "color": "#E7E6E6"
    },
    "alignment": {
      "horizontal": "right",
      "vertical": "center"
    }
  },
  "note": {
    "font": {
      "name": "Arial",
      "size": 9,
      "italic": true,
      "color": "#808080"
    },
    "alignment": {
      "horizontal": "left",
      "vertical": "top",
      "wrap_text": true
    }
  }
}
```

**Using custom presets:**
```bash
python excel_processor.py input.xlsx commands.json --presets my_themes.json
```

**In your commands JSON:**
```json
{
  "command": "set_theme",
  "sheet": "Sheet1",
  "row": 1,
  "column": 1,
  "theme": "company_header"
}
```

**Custom preset properties:**
- `font`: Object with `name`, `size`, `bold`, `italic`, `underline`, `color`
- `fill`: Object with `color` (hex color for cell background)
- `alignment`: Object with `horizontal`, `vertical`, `wrap_text`

Custom presets can override built-in presets by using the same name. See `example_presets.json` for a complete example.

## Status File

The script **always creates** a status file to track execution results.

**Format:**
- **Success**: Contains a single line with `0`
- **Failure**: Contains `1` on the first line, followed by error details on subsequent lines

**Default location:** `status.txt` in the same directory as the Excel file

**Custom location:** Use `--status-file` argument to specify a different path

**Example success status file:**
```
0
```

**Example failure status file:**
```
1
Error executing command 3 (set_cell_text): Sheet 'InvalidSheet' not found
Error executing command 5 (delete_row): row must be > 0
```

## Exit Codes

- `0`: All commands executed successfully
- `1`: One or more errors occurred (see status file for details)

## Error Handling

The script uses a **continue-on-error** approach:

1. Commands execute sequentially in the order specified
2. If a command fails, the error is logged but execution continues
3. All errors are collected during execution
4. At the end, all errors are reported together
5. If any errors occurred, the script exits with code 1
6. Status file contains all error details

This allows you to see all issues at once rather than fixing them one at a time.

## Example

See `example_commands.json` for a complete example demonstrating all features.
