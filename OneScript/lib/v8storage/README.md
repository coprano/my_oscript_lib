# v8storage
[![Stars](https://img.shields.io/github/stars/khorevaa/v8storage.svg?label=Github%20%E2%98%85&a)](https://github.com/khorevaa/v8storage/stargazers)
[![Release](https://img.shields.io/github/tag/khorevaa/v8storage.svg?label=Last%20release&a)](https://github.com/khorevaa/v8storage/releases)
[![Открытый чат проекта https://gitter.im/EvilBeaver/oscript-library](https://badges.gitter.im/khorevaa/v8storage.png)](https://gitter.im/EvilBeaver/oscript-library)

[![Build Status](https://travis-ci.org/khorevaa/v8storage.svg?branch=master)](https://travis-ci.org/khorevaa/v8storage)
[![Coverage Status](https://coveralls.io/repos/github/khorevaa/v8storage/badge.svg?branch=master)](https://coveralls.io/github/khorevaa/v8storage?branch=master)

## Библиотека для упрощения работы с Хранилищем 1С из oscript.

Позволяет выполнять рутинные операции с Хранилищем 1С в стиле [v8runner](https://github.com/oscript-library/v8runner).

Пример работы:
```bsl
ХранилищеКонфигурации = Новый МенеджерХранилищаКонфигурации();
ХранилищеКонфигурации.УстановитьПутьКХранилищу(КаталогХранилища);

ХранилищеКонфигурации.ПрочитатьХранилище();

ХранилищеКонфигурации.СохранитьВерсиюКонфигурацииВФайл(НомерВерсии, ИмяФайлаКофигурации);

ТаблицаВерсий = ХранилищеКонфигурации.ПолучитьТаблицаВерсий();
МассивАвторов = ХранилищеКонфигурации.ПолучитьАвторов();

```

Так же описание функциональности содержится в папке `features`. В прилагающихся `step_definitions` можно подсмотреть больше примеров.

## Публичный интерфейс

### Класс МенеджерХранилищаКонфигурации:

> Работа со свойствами объекта МенеджерХранилищаКонфигурации

#### УстановитьУправлениеКонфигуратором
```bsl
// Установка управления конфигуратором в класс менеджер хранилища конфигурации
//
// Параметры:
//   НовыйУправлениеКонфигуратором - класс - инстанс класс УправлениеКонфигуратором из библиотеке v8runner
//
```

#### ПолучитьУправлениеКонфигуратором
```bsl
// Получает управления конфигуратором используемое в менеджере хранилища конфигурации
//
```

#### УстановитьПутьКХранилищу
```bsl
// Установка путь к хранилищу конфигурации
//
// Параметры:
//   НовыйПутьКХранилищу - Строка - путь к хранилищу конфигурации 1С
//
```

#### УстановитьПараметрыАвторизации
```bsl
// Установка авторизации в хранилище конфигурации
//
// Параметры:
//   Пользователь - Строка - пользователь хранилищем конфигурации 1С
//   Пароль - Строка - пароль пользователя хранилищем конфигурации 1С (по умолчанию пустая строка)
//
```

#### ЗахватитьОбъектыВХранилище
```bsl
// Захват объектов для редактирования в хранилище конфигурации
//
// Параметры:
//  ПутьКФайлуСоСпискомОбъектов - Строка - Строка путь к файлу xml c содержанием в формате http://its.1c.ru/db/v839doc#bookmark:adm:TI000000712
// 									 путь к файлу формата XML со списком объектов. Если опция используется, будет выполнена попытка захватить только объекты,
//									 указанные в файле. Если опция не используется, будут захвачены все объекты конфигурации.
//									 Если в списке указаны объекты, захваченные другим пользователем, эти объекты не будут захвачены и будет выдана ошибка.
//									 При этом доступные для захвата объекта будут захвачены. Подробнее о формате файла см в документации.
//  ПолучатьЗахваченныеОбъекты  - булево - Флаг получения захваченных объектов (По умолчанию равно "Ложь")
//
```

#### ОтменитьЗахватОбъектовВХранилище
```bsl
// Отмена захват объектов для редактирования в хранилище конфигурации
//
// Параметры:
//  СписокОбъектов  	  - Строка - Строка путь к файлу xml c содержанием в формате http://its.1c.ru/db/v839doc#bookmark:adm:TI000000712
// 									 Если опция используется, будет выполнена попытка отменить захват только для объектов, указанных в файле.
//									 Если опция не используется, захват будет отменен для всех объектов конфигурации.
//									 При наличии в списке объектов, не захваченных текущим пользователем или захваченных другим пользователем, ошибка выдана не будет
//  ИгнорироватьИзменения - булево - Флаг игнорирования локальных изменений (По умолчанию равно "Ложь")
//									 Локально измененные объекты будут получены из хранилища, и внесенные изменения будут потеряны.
//									 Если опция не указана, то при наличии локально измененных объектов операция будет отменена и будет выдана ошибка.
//
```
#### ПоместитьИзмененияОбъектовВХранилище
```bsl
// Помещение изменений объектов в хранилище конфигурации
//
// Параметры:
//  СписокОбъектов  	  - Строка - Строка путь к файлу xml c содержанием в формате http://its.1c.ru/db/v839doc#bookmark:adm:TI000000712
//                                   Если опция используется, будет выполнена попытка поместить только объекты, указанные в файле.
//                                   Если опция не используется, будут помещены изменения всех объектов конфигурации.
//                                   При наличии в списке объектов, не захваченных текущим пользователем или захваченных другим пользователем, ошибка выдана не будет
//  Комментарий	 	      - Строка - Комментарий к помещаемым. Чтобы установить многострочный комментарий, для каждой строки следует использовать свою опцию comment.
//  ОставитьОбъектыЗахваченными  - булево - оставлять захват для помещенных объектов.
//  ИгнорироватьУдаленные - булево - Флаг игнорирования удаления объектов. По умолчанию = Ложь
//                                   Если опция используется, при обнаружении ссылок на удаленные объекты будет выполнена попытка их очистить.
//                                   Если опция не указана, при обнаружении ссылок на удаленные объекты будет выдана ошибка.
//
```

#### ПолучитьВыводКоманды
```bsl
// Возвращает вывод выполнения команды конфигуратора
//
```

#### СоздатьХранилищеКонфигурации
```bsl
// Создание файлового хранилища конфигурации используя контекст конфигуратора
//
// Параметры:
//  ПодключитьБазуКхранилищу  - булево - признак необходимости подключения базы контекста к хранилищу (по умолчанию ложь)
```

#### УстановитьМеткуДляВерсииВХранилище
```bsl
// Установка метки для версии хранилища
//
// Параметры:
//  Метка  	  			  - Строка - текст метки
//  Комментарий  	  	  - Строка - текст комментария к устанавливаемой метки.
//  Версия  	  	   	  - Строка - номер версии хранилища, для которого устанавливается метка.
//									Если версия не указана, метка ставится для самой последнее версии хранилища.
//									Если указана несуществующая версия, выдается ошибка
//
```

#### ДобавитьПользователяВХранилище
```bsl
// Добавление пользователя хранилища конфигурации.
//	Пользователь, от имени которого выполняется подключение к хранилищу, должен обладать административными правами.
//	Если пользователь с указанным именем существует, то пользователь добавлен не будет.
// Параметры:
//   НовыйПользователь - Строка - Имя создаваемого пользователя.
//   ПарольПользователя - Строка - Пароль создаваемого пользователя.
//   Право - ПраваПользователяХранилища - Права пользователя. Возможные значения:
// 		ТолькоЧтение — право на просмотр, (по умолчанию)
// 		ПравоЗахватаОбъектов — право на захват объектов,
// 		ПравоИзмененияВерсий — право на изменение состава версий,
// 		Администрирование — право на административные функции.
// 	 ВосстановитьУдаленного - Булево - флаг небходимости востановления удаленного пользователя
//								       Если обнаружен удаленный пользователь с таким же именем, он будет восстановлен.
//
```

#### КопироватьПользователейИзХранилища
```bsl
// Копирование пользователей из хранилища конфигурации. Копирование удаленных пользователей не выполняется.
//   Если пользователь с указанным именем существует, то пользователь не будет добавлен.
//
//Параметры:
//   СтрокаСоединенияХранилищаКопии - Строка - Путь к хранилищу, из которого выполняется копирование пользователей.
//   ПользовательХранилищаКопии - Строка - Имя пользователя хранилища, из которого выполняется копирование пользователей.
//   ПарольХранилищаКопии - Строка - Пароль пользователя хранилища, из которого выполняется копирование пользователей.
//   ВосстановитьУдаленного - Булево - флаг небходимости востановления удаленных пользователей
//
```
#### ОптимизироватьБазуХранилища
```bsl
// Выполняет оптимизацию хранения базы данных хранилища конфигурации.
//
```

#### ПраваПользователяХранилища
```bsl
// Возвращает структура возможных прав пользователя в хранилище конфигурации
//   Ключи структуры:
// 		ТолькоЧтение — право на просмотр, (по умолчанию)
// 		ПравоЗахватаОбъектов — право на захват объектов,
// 		ПравоИзмененияВерсий — право на изменение состава версий,
// 		Администрирование — право на административные функции.
//
```

#### СохранитьВерсиюКонфигурацииВФайл
```bsl
// Сохранение в файл версии конфигурации из хранилища
//
// Параметры:
//   НомерВерсии - число/строка - номер версии в хранилище
//   ИмяФайлаКофигурации - строка - путь к файлу в который будет сохранена версия конфигурации из хранилища
//
```

#### ПоследняяВерсияКонфигурацииВФайл
```bsl
// Сохранение в файл последней версии конфигурации из хранилища
// (обертка над процедурой "СохранитьВерсиюКонфигурацииВФайл")
// Параметры:
//   ИмяФайлаКофигурации - строка - путь к файлу в который будет сохранена версия конфигурации из хранилища
//
```

#### ПрочитатьХранилище
```bsl
// Чтение данных по истории версий и авторов из хранилища
//
// Параметры:
//   НомерНачальнойВерсии - число - номер версии хранилища,
//                                  с которой производиться получение истории (по умолчанию 1)
//
```

#### ПолучитьТаблицуВерсий
```bsl
// Получение таблицы истории версий из хранилища
// (выполняет ПрочитатьХранилище(1), если еще не было чтения)
//
// Возвращаемое значение таблица значений:
//   Колонки:
//      Номер   - число - номер версии
//      Дата    - Дата - Дата версии
//      Автор   - строка - автор версии
//      Комментарий   - Строка - многострочная строка с комментарием к версии
//
```

#### ПолучитьАвторов
```bsl
// Получение массива авторов версий из хранилища
// (выполняет ПрочитатьХранилище(1), если еще не было чтения)
//
// Возвращаемое значение массив:
//      Автор - строка - используемые авторы в хранилище
//
```

#### ПолучитьОтчетПоВерсиям
```bsl
/// Получение отчет по истории версий  из хранилища
//
// Параметры:
//   ПутьКФайлуРезультата - Строка - путь к файлу в который будет выгружен отчет,
//   НомерНачальнойВерсии - число - номер начальной версии хранилища,
//                                  с которой производиться получение истории (по умолчанию 1)
//   НомерКонечнойВерсии  - число - номер конечной версии хранилища. (по умолчанию - Неопределено)
//
```

#### ПодключитьсяКХранилищу
```bsl
// Выполняет подключение ранее неподключенной информационной базы к хранилищу конфигурации.
//
// Параметры:
//  ИгнорироватьНаличиеПодключеннойБД  - Булево - Флаг игнорирования наличия уже у пользователя уже подключенной базы данных. По умолчанию = Ложь
//								 	 Выполняет подключение даже в том случае, если для данного пользователя уже есть конфигурация, связанная с данным хранилищем..
//  ЗаменитьКонфигурациюБД - Булево - Флаг замены конфигурации БД на конфигурацию хранилища  (По умолчанию Истина)
//									 Если конфигурация непустая, данный ключ подтверждает замену конфигурации на конфигурацию из хранилища.
//
```

#### ОтключитьсяОтХранилища
```bsl
// Выполняет отключение ранее подключенной информационной базы (база контекста) к хранилищу конфигурации.
//
```

#### СконвертироватьОтчет
```bsl
// Получение отчет по истории версий  из хранилища
//
// Параметры:
//   ПутьКФайлуРезультата - Строка - путь к файлу отчета в формате mxl
//   ПутьКФайлуОтчетаJSON - Строка - путь к файлу в который будет выгружен отчет в формате json,
//
```

#### ПолучитьТаблицуЗахваченныхОбъектов
```bsl
// Возвращает таблицу захваченных объектов объектов в хранилище, согласно тексту лога захвата
//
// Параметры:
//  ТекстЛога - строка - строка вывода результат выполенния команды захвата в хранилище
//
// Возвращаемое значение:
//  ТаблицаЗначений:
//    ПолноеИмя - строка - например, Документы.Документ1.Формы.ФормаДокумента1
//    ЗахваченДляРедактирования - булево - признак успешного захвата в хранилище
//
```

### Класс СписокОбъектовКонфигурации:

Работа со спиской объектов конфигурации для захвата и помещения в хранилище

#### ПолучитьТаблицуОбъектов
```bsl
// Возвращает таблицу объектов следующего формата
//  ТаблицаЗначений:
//    ПолноеИмя - строка - например, Документы.Документ1.Формы.ФормаДокумента1
//    ПолноеИмяФайла - строка - путь к файлу исходников
//    ПолноеИмяВоВторойКонфигурации - строка - аналогично, "ПолноеИмя"
//    ВключатьПодчиненные - булево - признак включения в работу подчиненных объектов
//    Подсистема - структура - ключи ТипКонфигурации, ВключитьВсеПодчиненныОбъекты
//
```

#### ДобавитьОбъектКонфигурации
```bsl
// Добавление объекта конфигурации в таблицу объектов, для последующей записи в файл 
//
// Параметры:
//    ПолноеИмя - строка - например, Документы.Документ1.Формы.ФормаДокумента1
//    ВключатьПодчиненные - булево - признак включения в работу подчиненных объектов
//    ПолноеИмяФайла - строка - путь к файлу исходников
//    ПолноеИмяВоВторойКонфигурации - строка - аналогично, "ПолноеИмя"
//
```

#### ДобавитьОписаниеКонфигурации
```bsl
// Добавление описания конфигурации (корень) для последующей записи в файл 
//
// Параметры:
//    ПолноеИмя - строка - например, Документы.Документ1.Формы.ФормаДокумента1
//    ВключатьПодчиненные - булево - признак включения в работу подчиненных объектов
//    ПолноеИмяФайла - строка - путь к файлу исходников
//
```

#### ДобавитьОбъектПодсистему
```bsl
// Добавление объекта конфигурации в таблицу объектов, для последующей записи в файл 
//
// Параметры:
//    ПолноеИмя - строка - например, Документы.Документ1.Формы.ФормаДокумента1
//    ВключатьПодчиненные - булево - признак включения в работу подчиненных объектов
//    ПолноеИмяФайла - строка - путь к файлу исходников
//    ТипКонфигурации - строка - ??
//    ПолноеИмяВоВторойКонфигурации - строка - аналогично, "ПолноеИмя"
//    ВключитьВсеПодчиненныОбъекты - булево - признак включения в работу всех объектов подчиненных подсистем
//
```

#### ЗаписатьФайлОбъектов
```bsl
// Установка каталога файлового хранилища конфигурации
//
// Параметры:
//   ПутьКФайлуОбъектов - Строка - путь к файлу для записи объектов в формате XML,
//                                 При передаче пустой строки запишет туда путь к временному файлу
//
```

#### СформироватьСписокОбъектов
```bsl
// Формирует список объектов для переданного массива путей
//
// Параметры:
//   МассивПутейКФайламКонфигруации - массив - массив полных путей к файлам выгрузки конфигруации
//   ПапкаВыгрузкиИсходников - Строка - путь к папке корня конфигруации
//
```