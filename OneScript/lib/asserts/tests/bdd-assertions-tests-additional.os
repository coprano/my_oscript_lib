Перем мОбъектТеста;


Функция ПолучитьСписокТестов(юТест) Экспорт
	ВсеТесты = Новый Массив;

	ВсеТесты.Добавить("ТестДолжен_Проверить_ИмеетМетод_НеВыбрасываетИсключениеДляСуществующегоМетода");
	ВсеТесты.Добавить("ТестДолжен_Проверить_ИмеетМетод_ВыбрасываетИсключениеДляОтсутствующегоМетода");
	ВсеТесты.Добавить("ТестДолжен_Проверить_ИмеетМетод_ВыбрасываетИсключениеСУказаннымТекстом");
	ВсеТесты.Добавить("ТестДолжен_Проверить_ИмеетМетод_ПоддерживаетОтрицание");
	ВсеТесты.Добавить("ТестДолжен_Проверить_ИмеетМетод_ПоддерживаетЦепныеВызовы");
	
	Возврат ВсеТесты;
КонецФункции


Процедура ТестДолжен_Проверить_ИмеетМетод_НеВыбрасываетИсключениеДляСуществующегоМетода() Экспорт
	мОбъектТеста
		.Что(Новый Массив)
		.ИмеетМетод("Добавить")
		;
КонецПроцедуры


Процедура ТестДолжен_Проверить_ИмеетМетод_ВыбрасываетИсключениеДляОтсутствующегоМетода() Экспорт
	Попытка
		мОбъектТеста
			.Что(Новый Массив)
			.ИмеетМетод("ТакогоИмениМетодаНеДолжноБыть");
	Исключение
		Возврат;
	КонецПопытки;

	// тест должен завершиться в обработке исключения
	// если дошло сюда - это ошибка
	ВызватьИсключение "Проверка существования у объекта несуществующего метода должна была выбросить исключение, но этого не произошло";
КонецПроцедуры


Процедура ТестДолжен_Проверить_ИмеетМетод_ВыбрасываетИсключениеСУказаннымТекстом() Экспорт
	Перем ЧастьТекста, Сообщение;

	ЧастьТекста = "ЭтотТекстДолженБытьВТекстеИсключения*#1~";
	Попытка
		мОбъектТеста
			.Что(Новый Массив, ЧастьТекста)
			.ИмеетМетод("ТакогоИмениМетодаНеДолжноБыть");
	Исключение
		Если 0 = СтрНайти(ОписаниеОшибки(), ЧастьТекста) Тогда
			Сообщение = "Ожидали, что проверка наличия несуществующего метода у объекта выбросит исключение с указанным текстом, но текст не был найден в тексте исключения" + Символы.ПС
						+ "Ожидаемый текст: " + ЧастьТекста + Символы.ПС
						+ "Текст исключения: " + ОписаниеОшибки();
			ВызватьИсключение Сообщение;
		Иначе
			Возврат;
		КонецЕсли;
	КонецПопытки;

	// тест должен завершиться в обработке исключения
	// если дошло сюда - это ошибка
	ВызватьИсключение "Проверка существования у объекта несуществующего метода должна была выбросить исключение, но этого не произошло";
КонецПроцедуры


Процедура ТестДолжен_Проверить_ИмеетМетод_ПоддерживаетОтрицание() Экспорт
	Попытка
		мОбъектТеста
			.Что(Новый Массив)
			.Не_()
			.ИмеетМетод("ТакогоИмениМетодаНеДолжноБыть");
	Исключение
		ВызватьИсключение "Ожидали, что проверка существования метода совместно с отрицанием не выбросит исключение. " + ОписаниеОшибки();
	КонецПопытки;
КонецПроцедуры


Процедура ТестДолжен_Проверить_ИмеетМетод_ПоддерживаетЦепныеВызовы() Экспорт
	Если ТипЗнч(мОбъектТеста.Что(Новый Массив).ИмеетМетод("Добавить")) <> Тип("БДДАссерт") Тогда
		ВызватьИсключение "Ожидали, что метод ИмеетМетод() поддерживает цепные вызовы (возвращает объект)";
	КонецЕсли;
КонецПроцедуры


Процедура Инициализация()
	мОбъектТеста = ЗагрузитьСценарий(ОбъединитьПути(ТекущийСценарий().Каталог, "..", "src", "bdd-asserts.os"));
КонецПроцедуры


Инициализация();