#Использовать ".."

Перем Парсер;

Процедура ОчиститьПоИмени()
	Результат = Парсер.НайтиПоИмени("FinDB");
	Если Результат = Неопределено Тогда
		Сообщить("Не найдена база с именем: FinDB");
	Иначе
		Сообщить("ID: " + Результат.ID);

		Чистильщик = Новый ОчисткаКеша();
		Чистильщик.УстановитьПарсер(Парсер);
		Чистильщик.ОчиститьКеш(Результат);
	КонецЕсли;
	
КонецПроцедуры

Процедура ОчиститьПоПутиФайловаяБД()

	Результат = Парсер.НайтиПоПути("C:\work\db\FinDB2\");
	Если Результат = Неопределено Тогда
		Сообщить("Не найдена база с адресом: " + "C:\work\db\FinDB2\");
	Иначе
		Сообщить("ID: " + Результат.ID);

		Чистильщик = Новый ОчисткаКеша();
		Чистильщик.УстановитьПарсер(Парсер);
		Чистильщик.ОчиститьКеш(Результат);

	КонецЕсли;

КонецПроцедуры

Процедура ОчиститьПоПутиВеб()

	Результат = Парсер.НайтиПоПути("http://localhost/lessons/");
	Если Результат = Неопределено Тогда
		Сообщить("Не найдена база с адресом: " + "http://localhost/lessons/");
	Иначе
		Сообщить("ID: " + Результат.ID);

		Чистильщик = Новый ОчисткаКеша();
		Чистильщик.УстановитьПарсер(Парсер);
		Чистильщик.ОчиститьКеш(Результат);

	КонецЕсли;

КонецПроцедуры

Процедура ОчиститьПоПутиСерверная()

	Результат = Парсер.НайтиПоПути("localhost:mysrvdata");
	Если Результат = Неопределено Тогда
		Сообщить("Не найдена база с адресом: " + "localhost:mysrvdata");
	Иначе
		Сообщить("ID: " + Результат.ID);

		Чистильщик = Новый ОчисткаКеша();
		Чистильщик.УстановитьПарсер(Парсер);
		Чистильщик.ОчиститьКеш(Результат);

	КонецЕсли;

КонецПроцедуры

Процедура ОчиститьВесьКеш()

	Чистильщик = Новый ОчисткаКеша();
	Чистильщик.УстановитьПарсер(Парсер);
	Чистильщик.ОчиститьВесьКеш();

КонецПроцедуры


Процедура Выполнить()

	ОчиститьПоИмени();
	ОчиститьПоПутиФайловаяБД();
	ОчиститьПоПутиВеб();
	ОчиститьПоПутиСерверная();
	ОчиститьВесьКеш();
	
КонецПроцедуры

Процедура Инициализация()

	Парсер = Новый ПарсерСпискаБаз;
	Парсер.УстановитьФайл("examples/ibases.v8i");

КонецПроцедуры

Инициализация();
Выполнить();