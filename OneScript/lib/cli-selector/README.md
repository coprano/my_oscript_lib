Интерактивный выбор значений в консоли
======================================

### Реализация класса `ВыборВКонсоли` для интерактивного мульти- или одиночного выбора значений в консоли.

- Операция мультивыбора возвращает массив выбранных значений.
- При одиночном выборе - выбранное значение.
- Для пунктов меню реализована возможность задавать начальную отметку и доступность изменения пункта меню

---

#### Примеры вызова операции выбора представлены в папке `/example`:
- [мультивыбор значений](examples/example_multi.os)
- [выбор одиночного значения](examples/example_single.os)

## Установка
- через пакетный менеджер opm командой  
`opm install cli-selector`
- вручную скачать файл cli-selector.ospx из раздела [release](https://github.com/oscript-library/cli-selector/releases)  
и установить его командой `opm install -f <путь к файлу>` 