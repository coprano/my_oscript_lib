# Краткое руководство

## Установка

1. Установите зависимости:
```bash
pip install openpyxl
```

Или при использовании виртуального окружения:
```bash
python3 -m venv venv
source venv/bin/activate  # В Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Базовый пример

1. **Создайте ваш Excel-файл** (например `data.xlsx`)

2. **Создайте JSON-файл с командами** (например `commands.json`):
```json
[
  {
    "command": "set_cell_text",
    "sheet": "Sheet1",
    "row": 1,
    "column": 1,
    "text": "Привет мир"
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

3. **Запустите скрипт**:
```bash
# Перезаписать исходный файл
python excel_processor.py data.xlsx commands.json

# Или сохранить в новый файл
python excel_processor.py data.xlsx commands.json -o output.xlsx

# С выводом отладки
python excel_processor.py data.xlsx commands.json --debug

# С пользовательскими темами
python excel_processor.py data.xlsx commands.json --presets my_themes.json
```

## Справочник команд

### 1. Установка текста ячейки
Устанавливает значение ячейки. Столбец можно указать числом или буквой.
```json
{
  "command": "set_cell_text",
  "sheet": "Sheet1",
  "row": 2,
  "column": 3,
  "text": "Ваш текст здесь"
}
```

Или используя буквенное обозначение:
```json
{
  "command": "set_cell_text",
  "sheet": "Sheet1",
  "row": 2,
  "column": "C",
  "text": "Ваш текст здесь"
}
```

### 2. Добавление строки
Вставляет новую строку после указанной строки.
```json
{
  "command": "add_row",
  "sheet": "Sheet1",
  "after_row": 5
}
```

### 3. Удаление строки
Удаляет указанную строку.
```json
{
  "command": "delete_row",
  "sheet": "Sheet1",
  "row": 3
}
```

### 4. Установка темы (готовая)
Применяет предопределенный стиль. Доступны: `header`, `title`, `highlight`, `warning`, `success`, `default`
```json
{
  "command": "set_theme",
  "sheet": "Sheet1",
  "row": 1,
  "column": "A",
  "theme": "header"
}
```

### 5. Установка темы (пользовательская)
Применяет пользовательское форматирование.
```json
{
  "command": "set_theme",
  "sheet": "Sheet1",
  "row": 2,
  "column": "A",
  "theme": {
    "font_name": "Arial",
    "font_size": 12,
    "bold": true,
    "font_color": "#FFFFFF",
    "bg_color": "#4472C4"
  }
}
```

### 6. Копирование формата
Копирует форматирование из одной ячейки в другую.
```json
{
  "command": "copy_format",
  "source_sheet": "Sheet1",
  "source_row": 1,
  "source_column": "A",
  "target_sheet": "Sheet1",
  "target_row": 10,
  "target_column": "A"
}
```

## Пользовательские темы

Вы можете создать свои собственные темы в отдельном JSON-файле:

**my_themes.json:**
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
  }
}
```

**Используйте с помощью:**
```bash
python excel_processor.py data.xlsx commands.json --presets my_themes.json
```

**Затем в ваших командах:**
```json
{
  "command": "set_theme",
  "sheet": "Sheet1",
  "row": 1,
  "column": 1,
  "theme": "company_header"
}
```

См. `example_presets.json` для дополнительных примеров.

## Файл статуса

Скрипт автоматически создает файл статуса (по умолчанию: `status.txt` в той же директории, что и ваш Excel-файл).

- **Успех**: Файл содержит `0`
- **Ошибка**: Файл содержит `1`, за которой следуют детали ошибок

Вы можете указать пользовательский файл статуса:
```bash
python excel_processor.py data.xlsx commands.json --status-file /path/to/status.txt
```

## Советы

- Нумерация строк и столбцов начинается с 1 (первая строка - 1, первый столбец - 1)
- Столбцы можно указывать числами (1, 2, 3...) или буквами ("A", "B", "C"...)
- Цвета можно указывать с `#` или без (оба варианта `#FF0000` и `FF0000` работают)
- Команды выполняются в порядке из JSON-массива
- Используйте флаг `--debug` для просмотра детальной информации о выполнении
- Скрипт проверяет имена листов и сообщит об ошибках, если листы не существуют

## Пример рабочего процесса

См. `example_commands.json` для полного рабочего примера, демонстрирующего все возможности.
