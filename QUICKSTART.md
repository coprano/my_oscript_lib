# Quick Start Guide

## Installation

1. Install dependencies:
```bash
pip install openpyxl
```

Or if using a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Basic Example

1. **Create your Excel file** (e.g., `data.xlsx`)

2. **Create a JSON commands file** (e.g., `commands.json`):
```json
[
  {
    "command": "set_cell_text",
    "sheet": "Sheet1",
    "row": 1,
    "column": 1,
    "text": "Hello World"
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

3. **Run the script**:
```bash
# Overwrite the original file
python excel_processor.py data.xlsx commands.json

# Or save to a new file
python excel_processor.py data.xlsx commands.json -o output.xlsx

# With debug output
python excel_processor.py data.xlsx commands.json --debug
```

## Command Reference

### 1. Set Cell Text
Sets the value of a cell.
```json
{
  "command": "set_cell_text",
  "sheet": "Sheet1",
  "row": 2,
  "column": 3,
  "text": "Your text here"
}
```

### 2. Add Row
Inserts a new row after the specified row.
```json
{
  "command": "add_row",
  "sheet": "Sheet1",
  "after_row": 5
}
```

### 3. Delete Row
Deletes a specific row.
```json
{
  "command": "delete_row",
  "sheet": "Sheet1",
  "row": 3
}
```

### 4. Set Theme (Preset)
Applies a predefined style. Available: `header`, `title`, `highlight`, `warning`, `success`, `default`
```json
{
  "command": "set_theme",
  "sheet": "Sheet1",
  "row": 1,
  "column": 1,
  "theme": "header"
}
```

### 5. Set Theme (Custom)
Applies custom formatting.
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
    "font_color": "#FFFFFF",
    "bg_color": "#4472C4"
  }
}
```

### 6. Copy Format
Copies formatting from one cell to another.
```json
{
  "command": "copy_format",
  "source_sheet": "Sheet1",
  "source_row": 1,
  "source_column": 1,
  "target_sheet": "Sheet1",
  "target_row": 10,
  "target_column": 1
}
```

## Status File

The script automatically creates a status file (default: `status.txt` in the same directory as your Excel file).

- **Success**: File contains `0`
- **Failure**: File contains `1` followed by error details

You can specify a custom status file:
```bash
python excel_processor.py data.xlsx commands.json --status-file /path/to/status.txt
```

## Tips

- Row and column numbers are 1-indexed (first row is 1, first column is 1)
- Colors can be specified with or without `#` (both `#FF0000` and `FF0000` work)
- Commands are executed in order from the JSON array
- Use `--debug` flag to see detailed execution information
- The script validates sheet names and will report errors if sheets don't exist

## Example Workflow

See `example_commands.json` for a complete working example that demonstrates all features.
