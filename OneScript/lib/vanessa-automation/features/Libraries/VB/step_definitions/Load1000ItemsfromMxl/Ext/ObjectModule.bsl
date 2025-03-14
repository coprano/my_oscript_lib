﻿
///////////////////////////////////////////////////
//Служебные функции и процедуры
///////////////////////////////////////////////////

// контекст фреймворка Vanessa-Behavior
Перем Ванесса;

// Служебная функция.
Функция ДобавитьШагВМассивТестов(МассивТестов,Снипет,ИмяПроцедуры,ПредставлениеТеста = Неопределено,Транзакция = Неопределено,Параметр = Неопределено)
	Структура = Новый Структура;
	Структура.Вставить("Снипет",Снипет);
	Структура.Вставить("ИмяПроцедуры",ИмяПроцедуры);
	Структура.Вставить("ИмяПроцедуры",ИмяПроцедуры);
	Структура.Вставить("ПредставлениеТеста",ПредставлениеТеста);
	Структура.Вставить("Транзакция",Транзакция);
	Структура.Вставить("Параметр",Параметр);
	МассивТестов.Добавить(Структура);
КонецФункции

// Делает отключение модуля
&НаКлиенте
Функция ОтключениеМодуля() Экспорт

	Ванесса = Неопределено;
	Контекст = Неопределено;
	КонтекстСохраняемый = Неопределено;

КонецФункции

// Функция экспортирует список шагов, которые реализованы в данной внешней обработке.
Функция ПолучитьСписокТестов(КонтекстФреймворкаBDD) Экспорт
	Ванесса = КонтекстФреймворкаBDD;
	
	ВсеТесты = Новый Массив;

	//описание параметров
	//ДобавитьШагВМассивТестов(ВсеТесты,Снипет,ИмяПроцедуры,ПредставлениеТеста,Транзакция,Параметр);

	ДобавитьШагВМассивТестов(ВсеТесты,"ИмеетсяМетаданное(Парам01)","ИмеетсяМетаданное","Дано:  Имеется метаданное ""Справочник1""");
	ДобавитьШагВМассивТестов(ВсеТесты,"СуществуетМакет(Парам01)","СуществуетМакет","и существует макет ""ТысячаЭлементовСправочника1""");
	ДобавитьШагВМассивТестов(ВсеТесты,"ЯЗагружаюМакет(Парам01)","ЯЗагружаюМакет","И я загружаю макет ""ТысячаЭлементовСправочника1""");
	ДобавитьШагВМассивТестов(ВсеТесты,"ВСпискеЭлементовСправочникаСуществуетНеМенееЭлементов(Парам01,Парам02)","ВСпискеЭлементовСправочникаСуществуетНеМенееЭлементов","Тогда В списке элементов справочника ""Справочник1"" существует не менее 1000 элементов");

	Возврат ВсеТесты;
КонецФункции
	
// Служебная функция для подключения библиотеки создания fixtures.
Функция ПолучитьМакетОбработки(ИмяМакета) Экспорт
	Возврат ПолучитьМакет(ИмяМакета);
КонецФункции



///////////////////////////////////////////////////
//Работа со сценариями
///////////////////////////////////////////////////

// Функция выполняется перед началом каждого сценария
Функция ПередНачаломСценария() Экспорт
	
КонецФункции

// Функция выполняется перед окончанием каждого сценария
Функция ПередОкончаниемСценария() Экспорт
	
КонецФункции



///////////////////////////////////////////////////
//Реализация шагов
///////////////////////////////////////////////////

//Дано:  Имеется метаданное "Справочник1"
//@ИмеетсяМетаданное(Парам01)
Функция ИмеетсяМетаданное(ИмяОбъекта) Экспорт
	
	Ванесса.ПроверитьНеРавенство(Метаданные.НайтиПоПолномуИмени(ИмяОбъекта),Неопределено);
	
КонецФункции

//и существует макет "ТысячаЭлементовСправочника1"
//@СуществуетМакет(Парам01)
Функция СуществуетМакет(ИмяМакета) Экспорт
	
	Попытка
		Макет = ПолучитьМакет(ИмяМакета);
	Исключение
		ТекстСообщения = Ванесса.ПолучитьТекстСообщенияПользователю("Не найден макет %1 ошибка: %2");
		ТекстСообщения = СтрЗаменить(ТекстСообщения,"%1",ИмяМакета);
		ТекстСообщения = СтрЗаменить(ТекстСообщения,"%2",ОписаниеОшибки());
		ВызватьИсключение ТекстСообщения;
	КонецПопытки;
	
КонецФункции

//И я загружаю макет "ТысячаЭлементовСправочника1"
//@ЯЗагружаюМакет(Парам01)
Функция ЯЗагружаюМакет(ИмяМакета) Экспорт
	Ошибка = """";
	Попытка
		ОбычнаяФормаВанессы 				= Ванесса.ПолучитьФорму("Форма");
		ОбработкаСвязаннаяСИсполняемойФичей = ОбычнаяФормаВанессы.ОбработкаСвязаннаяСИсполняемойФичей; 
		Макет 								= ОбработкаСвязаннаяСИсполняемойФичей.ПолучитьМакетОбработки(ИмяМакета);
		СтруктураДанных 					= Ванесса.СоздатьДанныеПоТабличномуДокументу(Макет);
		Ванесса.ПроверитьНеРавенство(СтруктураДанных,Неопределено,"Получили структуру данных.");
	Исключение
		Ошибка = СокрЛП(ОписаниеОшибки());  		
		ТекстСообщения = Ванесса.ПолучитьТекстСообщенияПользователю("Шаг выполнен с ошибкой: %1");
		ТекстСообщения = СтрЗаменить(ТекстСообщения,"%1",Ошибка);
		ВызватьИсключение ТекстСообщения;
	КонецПопытки;  
КонецФункции

//Тогда В списке элементов справочника "Справочник1" существует не менее 1000 элементов
//@ВСпискеЭлементовСправочникаСуществуетНеМенееЭлементов(Парам01,Парам02)
Функция ВСпискеЭлементовСправочникаСуществуетНеМенееЭлементов(ИмяСправочника,Количество) Экспорт
	
	Запрос = Новый Запрос;
	Запрос.Текст = 
	"ВЫБРАТЬ
	|	КОЛИЧЕСТВО(*) КАК Счетчик
	|ИЗ
	|	Справочник."+ИмяСправочника+" КАК ИмяСправочника";
	
	РезультатЗапроса = Запрос.Выполнить();
	
	ВыборкаДетальныеЗаписи = РезультатЗапроса.Выбрать();
	
	ВыборкаДетальныеЗаписи.Следующий();
	
	СуществуетЭлементов = ВыборкаДетальныеЗаписи.Счетчик;
	
	Ванесса.ПроверитьРавенство(СуществуетЭлементов>Количество, Истина)

	
КонецФункции
