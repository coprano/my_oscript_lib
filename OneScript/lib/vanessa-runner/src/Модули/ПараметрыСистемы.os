///////////////////////////////////////////////////////////////////
//
// Служебный модуль с набором служебных параметров приложения
//
// Структура модуля реализована в соответствии с рекомендациями
// oscript-app-template (C) EvilBeaver
//
///////////////////////////////////////////////////////////////////
#Использовать packageinfo

Перем КорневойПутьПроекта Экспорт;
Перем ЭтоWindows Экспорт;

Перем мВозможныеКоманды;

//	Возвращает идентификатор лога приложения
//
// Возвращаемое значение:
//   Строка   - Значение идентификатора лога приложения
//
Функция ИмяЛогаСистемы() Экспорт

	Возврат "oscript.app." + ИмяПродукта();

КонецФункции

//	Возвращает текущую версию продукта
//
// Возвращаемое значение:
//   Строка   - Значение текущей версии продукта
//
Функция ВерсияПродукта() Экспорт

	// Указываем путь до packagedef с информацией о приложении.
	ПутьКМанифесту = ОбъединитьПути(ТекущийСценарий().Каталог, "..", "..", "packagedef");

	ОписаниеПакета = Новый ИнформацияОПакете(ПутьКМанифесту);
  
	Возврат ОписаниеПакета.Версия();

КонецФункции

// Возвращает имя продукта
//
//  Возвращаемое значение:
//   Строка - имя продукта
//
Функция ИмяПродукта() Экспорт
	Возврат "vanessa-runner";
КонецФункции

Функция ВозможныеКоманды() Экспорт

	Если мВозможныеКоманды = Неопределено Тогда

		мВозможныеКоманды = Новый Структура;
		мВозможныеКоманды.Вставить("СоздатьПроект", "init-project");

		мВозможныеКоманды.Вставить("ИнициализацияОкружения", "init-dev");
		мВозможныеКоманды.Вставить("ОбновлениеОкружения", "update-dev");

		мВозможныеКоманды.Вставить("СборкаВнешнихОбработок", "compileepf");
		мВозможныеКоманды.Вставить("РазборкаВнешнихОбработок", "decompileepf");

		мВозможныеКоманды.Вставить("Тестирование_xUnitFor1C", "xunit");
		мВозможныеКоманды.Вставить("ТестироватьПоведение", "vanessa");

		мВозможныеКоманды.Вставить("СборкаРасширений", "compileext");
		мВозможныеКоманды.Вставить("РазборкаРасширений", "decompileext");
		мВозможныеКоманды.Вставить("ЗагрузитьРасширениеИзФайла", "loadext");
		мВозможныеКоманды.Вставить("ВыгрузитьРасширениеВФайл", "unloadext");
		мВозможныеКоманды.Вставить("ОбновлениеРасширений", "updateext");
		мВозможныеКоманды.Вставить("СобратьИзИсходниковФайлРасширения", "compileexttocfe");

		мВозможныеКоманды.Вставить("ЗапуститьВРежимеПредприятия", "run");
		мВозможныеКоманды.Вставить("ЗапуститьКонфигуратор", "designer");
		мВозможныеКоманды.Вставить("ОбновитьКонфигурациюБазыДанных", "updatedb");
		мВозможныеКоманды.Вставить("ВыгрузитьКонфигурациюВФайл", "unload");
		мВозможныеКоманды.Вставить("СоздатьФайлПоставки", "make-dist");
		мВозможныеКоманды.Вставить("ВыгрузитьИнфобазуВФайл", "dump");
		мВозможныеКоманды.Вставить("ЗагрузитьИнфобазуИзФайла", "restore");
		мВозможныеКоманды.Вставить("СоздатьИнформационнуюБазу", "create");
		мВозможныеКоманды.Вставить("УдалитьИнформационнуюБазу", "remove");
		мВозможныеКоманды.Вставить("ПроверкаСинтаксиса", "syntax-check");

		мВозможныеКоманды.Вставить("ОбновитьИзХранилища", "loadrepo");
		мВозможныеКоманды.Вставить("СоздатьХранилище", "createrepo");
		мВозможныеКоманды.Вставить("ПодключитьсяКХранилищу", "bindrepo");
		мВозможныеКоманды.Вставить("СоздатьПользователейХранилища", "createrepouser");
		мВозможныеКоманды.Вставить("КопироватьПользователейХранилища", "copyrepouser");
		мВозможныеКоманды.Вставить("СохранитьВерсиюХранилищаВФайл", "unloadcfrepo");
		мВозможныеКоманды.Вставить("ЗахватитьВХранилище", "lockrepo");
		мВозможныеКоманды.Вставить("ПоместитьВХранилище", "commit");
		мВозможныеКоманды.Вставить("ОтключитьсяОтХранилища", "unbindrepo");
		мВозможныеКоманды.Вставить("ОтпуститьВХранилище", "unlockrepo");

		мВозможныеКоманды.Вставить("СобратьИзИсходниковФайлКонфигурации", "compile");
		мВозможныеКоманды.Вставить("РазборкаКонфигурации", "decompile");
		мВозможныеКоманды.Вставить("ЗагрузитьФайлКонфигурации", "load");
		мВозможныеКоманды.Вставить("ОбъединитьСФайломКонфигурации", "merge");
		мВозможныеКоманды.Вставить("ОбновитьКонфигурацию", "update");
		мВозможныеКоманды.Вставить("СравнитьКонфигурации", "compare");

		мВозможныеКоманды.Вставить("УправлениеСеансами", "session");
		мВозможныеКоманды.Вставить("УправлениеРегламентнымиЗаданиями", "scheduledjobs");

		мВозможныеКоманды.Вставить("ЗапроситьПараметрыБД", "dbinfo");

		мВозможныеКоманды.Вставить("Помощь", "help");
		мВозможныеКоманды.Вставить("ПомощьУстаревшая", "--help");
		мВозможныеКоманды.Вставить("ПоказатьВерсию", "version");

		мВозможныеКоманды.Вставить("ПроверкаПроектаEDT", "edt-validate");

		мВозможныеКоманды.Вставить("УстановкаВерсии", "set-version");

		мВозможныеКоманды = Новый ФиксированнаяСтруктура(мВозможныеКоманды);

	КонецЕсли;

	Возврат мВозможныеКоманды;

КонецФункции

Процедура ПриРегистрацииКомандПриложения(Знач КлассыРеализацииКоманд) Экспорт

	КлассыРеализацииКоманд[ВозможныеКоманды().Помощь]					= "КомандаСправкаПоПараметрам";
	КлассыРеализацииКоманд[ВозможныеКоманды().ПомощьУстаревшая]			= "КомандаСправкаПоПараметрам";
	КлассыРеализацииКоманд[ИмяКомандыВерсия()]							= "КомандаVersion";
	КлассыРеализацииКоманд[ВозможныеКоманды().СоздатьПроект]			= "КомандаСоздатьПроект";
	КлассыРеализацииКоманд[ВозможныеКоманды().ИнициализацияОкружения]	= "КомандаИнициализацияОкружения";
	КлассыРеализацииКоманд[ВозможныеКоманды().ОбновлениеОкружения]		= "КомандаОбновлениеОкружения";

	КлассыРеализацииКоманд[ВозможныеКоманды().Тестирование_xUnitFor1C]	= "КомандаТестирование_xUnitFor1C";
	КлассыРеализацииКоманд[ВозможныеКоманды().ТестироватьПоведение]		= "КомандаТестированиеПоведения";
	КлассыРеализацииКоманд[ВозможныеКоманды().ЗапуститьВРежимеПредприятия]	= "КомандаЗапуститьВРежимеПредприятия";
	КлассыРеализацииКоманд[ВозможныеКоманды().ЗапуститьКонфигуратор]	= "КомандаЗапуститьКонфигуратор";

	КлассыРеализацииКоманд[ВозможныеКоманды().СборкаРасширений]			= "КомандаСборкаРасширений";
	КлассыРеализацииКоманд[ВозможныеКоманды().ЗагрузитьРасширениеИзФайла]			= "КомандаЗагрузитьРасширениеИзФайла";
	КлассыРеализацииКоманд[ВозможныеКоманды().ОбновлениеРасширений]			= "КомандаОбновлениеРасширений";
	КлассыРеализацииКоманд[ВозможныеКоманды().СобратьИзИсходниковФайлРасширения]	=
		"КомандаСобратьИзИсходниковФайлРасширения";
	КлассыРеализацииКоманд[ВозможныеКоманды().РазборкаРасширений]			= "КомандаРазборкаРасширений";
	КлассыРеализацииКоманд[ВозможныеКоманды().ВыгрузитьРасширениеВФайл]	= "КомандаВыгрузитьРасширениеВФайл";
	КлассыРеализацииКоманд[ВозможныеКоманды().СборкаВнешнихОбработок]	= "КомандаСборкаВнешнихОбработок";
	КлассыРеализацииКоманд[ВозможныеКоманды().РазборкаВнешнихОбработок]	= "КомандаРазборкаВнешнихОбработок";

	КлассыРеализацииКоманд[ВозможныеКоманды().ОбновитьКонфигурациюБазыДанных]	= "КомандаОбновлениеКонфигурацииБД";
	КлассыРеализацииКоманд[ВозможныеКоманды().ВыгрузитьКонфигурациюВФайл]	= "КомандаВыгрузитьКонфигурациюВФайл";
	КлассыРеализацииКоманд[ВозможныеКоманды().СоздатьФайлПоставки]	= "КомандаСоздатьФайлПоставки";
	КлассыРеализацииКоманд[ВозможныеКоманды().ВыгрузитьИнфобазуВФайл]	= "КомандаВыгрузитьИнфобазуВФайл";
	КлассыРеализацииКоманд[ВозможныеКоманды().ЗагрузитьИнфобазуИзФайла]	= "КомандаЗагрузитьИнфобазуИзФайла";
	КлассыРеализацииКоманд[ВозможныеКоманды().СоздатьИнформационнуюБазу] = "КомандаСоздатьИнформационнуюБазу";
	КлассыРеализацииКоманд[ВозможныеКоманды().УдалитьИнформационнуюБазу] = "КомандаУдалитьИнформационнуюБазу";

	КлассыРеализацииКоманд[ВозможныеКоманды().ОбновитьИзХранилища]	= "КомандаОбновитьИзХранилища";
	КлассыРеализацииКоманд[ВозможныеКоманды().СоздатьХранилище]	= "КомандаСоздатьХранилище";
	КлассыРеализацииКоманд[ВозможныеКоманды().ПодключитьсяКХранилищу]	= "КомандаПодключитьсяКХранилищу";
	КлассыРеализацииКоманд[ВозможныеКоманды().СоздатьПользователейХранилища]	=
		"КомандаСоздатьПользователейХранилища";
	КлассыРеализацииКоманд[ВозможныеКоманды().КопироватьПользователейХранилища]	=
		"КомандаКопироватьПользователейХранилища";
	КлассыРеализацииКоманд[ВозможныеКоманды().СохранитьВерсиюХранилищаВФайл]	=
		"КомандаСохранитьВерсиюХранилищаВФайл";
	КлассыРеализацииКоманд[ВозможныеКоманды().ЗахватитьВХранилище]	= "КомандаЗахватитьВХранилище";
	КлассыРеализацииКоманд[ВозможныеКоманды().ПоместитьВХранилище]	= "КомандаПоместитьВХранилище";
	КлассыРеализацииКоманд[ВозможныеКоманды().ОтключитьсяОтХранилища]	= "КомандаОтключитьсяОтХранилища";
	КлассыРеализацииКоманд[ВозможныеКоманды().ОтпуститьВХранилище] = "КомандаОтпуститьВХранилище";

	КлассыРеализацииКоманд[ВозможныеКоманды().СобратьИзИсходниковФайлКонфигурации]	= "КомандаСобратьИзИсходников";
	КлассыРеализацииКоманд[ВозможныеКоманды().РазборкаКонфигурации]	= "КомандаРазборкаКонфигурации";
	КлассыРеализацииКоманд[ВозможныеКоманды().ЗагрузитьФайлКонфигурации] = "КомандаЗагрузитьФайлКонфигурации";
	КлассыРеализацииКоманд[ВозможныеКоманды().ОбъединитьСФайломКонфигурации] = "КомандаОбъединитьСФайломКонфигурации";
	КлассыРеализацииКоманд[ВозможныеКоманды().ОбновитьКонфигурацию] = "КомандаОбновитьКонфигурацию";
	КлассыРеализацииКоманд[ВозможныеКоманды().СравнитьКонфигурации] = "КомандаСравнитьКонфигурации";

	КлассыРеализацииКоманд[ВозможныеКоманды().УправлениеСеансами] = "КомандаУправлениеСеансами";
	КлассыРеализацииКоманд[ВозможныеКоманды().УправлениеРегламентнымиЗаданиями] = "КомандаУправлениеСеансами";
	КлассыРеализацииКоманд[ВозможныеКоманды().ЗапроситьПараметрыБД] = "КомандаУправлениеСеансами";

	КлассыРеализацииКоманд[ВозможныеКоманды().ПроверкаСинтаксиса]	= "КомандаПроверкаСинтаксиса";
	КлассыРеализацииКоманд[ВозможныеКоманды().ПроверкаПроектаEDT]	= "КомандаПроверкаПроектаEDT";

	КлассыРеализацииКоманд[ВозможныеКоманды().УстановкаВерсии]	= "КомандаУстановкаВерсии";
	//...
    //КлассыРеализацииКоманд["<имя команды>"]	= "<КлассРеализации>";

КонецПроцедуры

// Одна из команд может вызываться неявно, без указания команды.
// Иными словами, здесь указывается какой обработчик надо вызывать, если приложение запущено без какой-либо команды
//  myapp /home/user/somefile.txt будет аналогично myapp default-action /home/user/somefile.txt
Функция ИмяКомандыПоУмолчанию() Экспорт
	Возврат ВозможныеКоманды().Помощь;
КонецФункции

// Возвращает имя команды версия (ключ командной строки)
//
//  Возвращаемое значение:
//   Строка - имя команды
//
Функция ИмяКомандыВерсия() Экспорт
	Возврат ВозможныеКоманды().ПоказатьВерсию;
КонецФункции

Процедура ПриРегистрацииГлобальныхПараметровКоманд(Знач Парсер) Экспорт
	Парсер.ДобавитьИменованныйПараметр("--ibconnection", "Строка подключения к БД (/FfilePath или /SserverPath)
		|	Например, для файловых баз --ibconnection /FC:\base1 или --ibconnection /F./base1 или --ibconnection /Fbase1
		|	Или для серверных баз --ibconnection /Sservername\basename", Истина);

	Парсер.ДобавитьИменованныйПараметр("--db-user", "Пользователь БД", Истина);
	Парсер.ДобавитьИменованныйПараметр("--db-pwd", "Пароль БД", Истина);
	Парсер.ДобавитьИменованныйПараметр("--v8version", "Версия платформы", Истина);
	Парсер.ДобавитьИменованныйПараметр("--bitness", "Разрядность платформы 1С. Варианты: x64,x86,x64x86,x86x64", Истина);
	Парсер.ДобавитьИменованныйПараметр("--additional",
		"Дополнительные параметры для передачи в 1С:Предприятие или Конфигуратор. Не для всех команд.", Истина);

	Парсер.ДобавитьИменованныйПараметр("--root", "Полный путь к проекту", Истина);
	Парсер.ДобавитьИменованныйПараметр("--ordinaryapp",
		"Запуск толстого клиента (1 = толстый, 0 = тонкий клиент, -1 = без указания клиента). По умолчанию используется значение 0 (тонкий клиент). Значение -1 может применяться в случаях, когда нужно прочитать лог работы 1С в режиме Предприятие в управляемом интерфейсе.",
		Истина);

	Парсер.ДобавитьПараметрФлаг("--nocacheuse",
		"Признак - не использовать кэш платформы для ускорения операций с базой,
		|а также не надо добавлять базу в список баз 1C пользователя", Истина);
	Парсер.ДобавитьИменованныйПараметр("--ibname", "(устарело) Строка подключения к БД", Истина);
	Парсер.ДобавитьИменованныйПараметр("--language", "Код языка запуска платформы", Истина);
	Парсер.ДобавитьИменованныйПараметр("--locale", "Код локализации сеанса платформы", Истина);

	Парсер.ДобавитьИменованныйПараметр("--uccode", "Ключ разрешения запуска", Истина);

	КаталогСценария = (Новый Файл(ТекущийСценарий().Источник)).Путь;
	ОбщиеМетоды1 = ЗагрузитьСценарий(ОбъединитьПути(КаталогСценария, "ОбщиеМетоды.os"));
	Парсер.ДобавитьИменованныйПараметр("--settings", "Путь к файлу настроек Vanessa-runner в формате json. По умолчанию имя файла " +
		ОбщиеМетоды1.ИмяФайлаНастроек(), Истина);

	Парсер.ДобавитьИменованныйПараметр("--debuglogfile", "Вывод отладочных файлов в указанный лог-файл", Истина);
	Парсер.ДобавитьПараметрФлаг("--debuglog",
		"Вывод отладочных файлов в лог-файл 'vrunner-XXX.log' во временном каталоге пользователя. ", Истина);
КонецПроцедуры
