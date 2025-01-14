﻿Перем БДД;
Перем Журнал;
Перем КлючЖурнала;

Функция ПолучитьСписокШагов(КонтекстФреймворкаBDD) Экспорт
	БДД = КонтекстФреймворкаBDD;

	ВсеШаги = Новый Массив;

	ВсеШаги.Добавить("ЯНичегоНеДелаю");
	ВсеШаги.Добавить("НичегоНеПроисходит");

	Возврат ВсеШаги;
КонецФункции

Процедура ЯНичегоНеДелаю(Знач ПарамСтрока) Экспорт
	ДобавитьВЖурнал("ЯНичегоНеДелаю", ПарамСтрока);
КонецПроцедуры

Процедура НичегоНеПроисходит(Знач ДругойПарамСтрока) Экспорт
	ДобавитьВЖурнал("НичегоНеПроисходит", ДругойПарамСтрока);

   Ожидаем.Что(Журнал[КлючЖурнала], "Ожидали, что журнал выполнения будет правильным, а это не так").Равно("ЯНичегоНеДелаю<ПарамСтрока>;НичегоНеПроисходит<ДругойПарамСтрока>;");
КонецПроцедуры

Процедура ДобавитьВЖурнал(Строка, Параметр = "") Экспорт
	Журнал.Вставить(КлючЖурнала, Журнал[КлючЖурнала]+Строка+"<"+Параметр+">;");
КонецПроцедуры

КлючЖурнала = (Новый Файл(ТекущийСценарий().Источник)).ИмяБезРасширения;
Журнал = Новый Соответствие;
Журнал.Вставить(КлючЖурнала, "");
