﻿#Использовать asserts
#Использовать ParserFileV8i

Процедура Инициализация()
	

КонецПроцедуры

Функция ПолучитьСписокТестов(Тестирование) Экспорт
	
	
	СписокТестов = Новый Массив;
	СписокТестов.Добавить("Тест_Должен_НайтиБазуПоИмени");
	СписокТестов.Добавить("Тест_Должен_НеНайтиБазуПоИмени");

	СписокТестов.Добавить("Тест_Должен_НайтиБазуПоПутиФайловая");
	СписокТестов.Добавить("Тест_Должен_НайтиБазуПоПутиВеб");
	СписокТестов.Добавить("Тест_Должен_НайтиБазуПоПутиСервер");
	СписокТестов.Добавить("Тест_Должен_ДобавитьБазуВСписокБаз");
		
	Возврат СписокТестов;
	
КонецФункции

Процедура Тест_Должен_НайтиБазуПоИмени() Экспорт
	
	Парсер = Новый ПарсерСпискаБаз;
	Парсер.УстановитьФайл("tests/ibases.v8i");

	Результат = Парсер.НайтиПоИмени("FinDB");

	//юТест.ПроверитьНеРавенство(Результат, Неопределено, "Не найдена база по имени");
	Ожидаем.Что(Результат).Существует();
	
КонецПроцедуры

Процедура Тест_Должен_НеНайтиБазуПоИмени() Экспорт
	
	Парсер = Новый ПарсерСпискаБаз;
	Парсер.УстановитьФайл("tests/ibases.v8i");

	Результат = Парсер.НайтиПоИмени("FinDB-3");

	//юТест.ПроверитьРавенство(Результат, Неопределено, "Найдена база по имени FinDB-3");
	Ожидаем.Что(Результат).Равно(Неопределено);
	
КонецПроцедуры

Процедура Тест_Должен_НайтиБазуПоПутиФайловая() Экспорт
	
	Парсер = Новый ПарсерСпискаБаз;
	Парсер.УстановитьФайл("tests/ibases.v8i");

	Результат = Парсер.НайтиПоПути("C:\work\db\FinDB");

	//юТест.ПроверитьНеРавенство(Результат, Неопределено, "Найдена база по пути");
	Ожидаем.Что(Результат).Существует();
	
КонецПроцедуры

Процедура Тест_Должен_НайтиБазуПоПутиВеб() Экспорт
	
	Парсер = Новый ПарсерСпискаБаз;
	Парсер.УстановитьФайл("tests/ibases.v8i");

	Результат = Парсер.НайтиПоПути("http://localhost/lessons/");

	//юТест.ПроверитьРавенство(Результат.Connect.String, "Connect=ws=""http://localhost/lessons/"";", "Найдена база по пути");
	Ожидаем.Что(Результат.Connect.String).Равно("Connect=ws=""http://localhost/lessons/"";");
	
КонецПроцедуры

Процедура Тест_Должен_НайтиБазуПоПутиСервер() Экспорт
	
	Парсер = Новый ПарсерСпискаБаз;
	Парсер.УстановитьФайл("tests/ibases.v8i");

	Результат = Парсер.НайтиПоПути("localhost:mysrvdata");

	//юТест.ПроверитьНеРавенство(Результат, Неопределено, "Найдена база по пути");
	Ожидаем.Что(Результат).Существует();
	
КонецПроцедуры

Процедура Тест_Должен_ДобавитьБазуВСписокБаз() Экспорт
	Парсер = Новый ПарсерСпискаБаз;
	Парсер.УстановитьФайл("tests/ibases.v8i");
	ИмяВременногоФайла = ПолучитьИмяВременногоФайла("v8i");

	ИмяБазы = "Теууууттттутт";
	СписокБаз = Парсер.ПолучитьСписокБаз();
	СтрокаПодключения = "Connect=File=""d:\temp\""";
	
	ОписаниеБазы = ОписаниеБазыВСписке(Неопределено);
	ОписаниеБазы.Вставить("Name", ИмяБазы);
	ОписаниеБазы.Вставить("Connect", Новый Структура("String", СтрокаПодключения));
	СписокБаз.Вставить(ИмяБазы, ОписаниеБазы);
	Парсер.ЗаписатьСписокБаз(СписокБаз, ИмяВременногоФайла);
	
	Парсер.УстановитьФайл(ИмяВременногоФайла);
	СписокБаз = Парсер.ПолучитьСписокБаз();
	Результат = Парсер.НайтиПоИмени(ИмяБазы);

	Ожидаем.Что(Результат).Существует();

КонецПроцедуры

Функция ОписаниеБазыВСписке(ДопПараметры)
	Результат = Новый Структура();
	Результат.Вставить("Connect","");
	// UUID генерим сразу, т.к. структура новая.
	Результат.Вставить("ID", Новый УникальныйИдентификатор()); 
	Результат.Вставить("OrderInList", ТекущаяУниверсальнаяДатаВМиллисекундах());
	Результат.Вставить("Folder", "/");
	Результат.Вставить("OrderInTree", ТекущаяУниверсальнаяДатаВМиллисекундах());
	Результат.Вставить("External", "0");
	Результат.Вставить("ClientConnectionSpeed", "Normal");
	Результат.Вставить("App", "Auto");
	Результат.Вставить("WA", "1");
	Результат.Вставить("Version", "");

	Возврат Результат;
КонецФункции //ОписаниеБазыВСписке


//////////////////////////////////////////////////////////////////////////////////////
// Инициализация

Инициализация();