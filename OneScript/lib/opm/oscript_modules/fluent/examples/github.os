#Использовать ".."
#Использовать notify

Перем Таблица;

Процедура ДобавитьСтрокуВТаблицу(Имя, Фолловеры, Местоположение, Контрибьюции);
	Строка = Таблица.Добавить();
	Строка.Имя = Имя;
	Строка.Фолловеры = Фолловеры;
	Строка.Местоположение = Местоположение;
	Строка.Контрибьюции = Контрибьюции;
КонецПроцедуры

Процедура Обработчик_ФильтрацияПоМестоположению(РезультатФильтрации, ДополнительныеПараметры) Экспорт
	РезультатФильтрации = ДополнительныеПараметры.Элемент.Местоположение = "Россия";
КонецПроцедуры

Процедура Обработчик_СортировкаПоФолловерам(РезультатСравнения, ДополнительныеПараметры) Экспорт
	РезультатСравнения = ДополнительныеПараметры.Элемент1.Фолловеры < ДополнительныеПараметры.Элемент2.Фолловеры;
КонецПроцедуры

Процедура Обработчик_СортировкаПоКонтрибьюциям(РезультатСравнения, ДополнительныеПараметры) Экспорт
	РезультатСравнения = ДополнительныеПараметры.Элемент1.Контрибьюции < ДополнительныеПараметры.Элемент2.Контрибьюции;
КонецПроцедуры

ФильтрацияПоМестоположению = Новый ОписаниеОповещения("Обработчик_ФильтрацияПоМестоположению", ЭтотОбъект);
СортировкаПоФолловерам = Новый ОписаниеОповещения("Обработчик_СортировкаПоФолловерам", ЭтотОбъект);
СортировкаПоКонтрибьюциям = Новый ОписаниеОповещения("Обработчик_СортировкаПоКонтрибьюциям", ЭтотОбъект);


Таблица = Новый ТаблицаЗначений;
Таблица.Колонки.Добавить("Имя");
Таблица.Колонки.Добавить("Фолловеры");
Таблица.Колонки.Добавить("Местоположение");
Таблица.Колонки.Добавить("Контрибьюции");

ДобавитьСтрокуВТаблицу("Иванов", 10, "Новая Зеландия", 45);
ДобавитьСтрокуВТаблицу("Петров", 0, "Россия", 50);
ДобавитьСтрокуВТаблицу("Сидоров", 15, "Россия", 12);
ДобавитьСтрокуВТаблицу("Туполев", 99, "Россия", 44);
ДобавитьСтрокуВТаблицу("Миль", 23, "Нидерланды", 31);
ДобавитьСтрокуВТаблицу("Сухой", 3, "Россия", 123);
ДобавитьСтрокуВТаблицу("Лавочкин", 10, "Россия", 68);
ДобавитьСтрокуВТаблицу("Яковлев", 12, "Россия", 99);


ПроцессорКоллекций = ПроцессорыКоллекций.ИзКоллекции(Таблица);
Результат = ПроцессорКоллекций
	.Фильтровать(ФильтрацияПоМестоположению)
	.Сортировать(СортировкаПоФолловерам)
	.Первые(5)
	.Сортировать(СортировкаПоКонтрибьюциям)
	.Первые(3)
	.Получить(Тип("ТаблицаЗначений"));

Для Каждого Элемент Из Результат Цикл
	Сообщить(Элемент.Имя);
КонецЦикла;

ПроцессорыКоллекций.ИзКоллекции(Таблица)
	.Фильтровать("Результат = Элемент.Местоположение = ""Россия""")
	.Сортировать("Результат = Элемент1.Фолловеры < Элемент2.Фолловеры")
	.Первые(5)
	.Сортировать("Результат = Элемент1.Контрибьюции < Элемент2.Контрибьюции")
	.Первые(3)
	.ДляКаждого("Сообщить(Элемент.Имя)");

// githubUsers
// 	.filter(_.location == 'Russia') 
//	.sort(_.followers)
// 	.take(1000)
// 	.sort(_.contributions)
// 	.take(256)