Перем мСообщенияЛога;

Функция ПолучитьСообщения() Экспорт
	Возврат мСообщенияЛога;
КонецФункции

////////////////////////////
// Методы аппендера

Процедура Вывести(Знач Сообщение, Знач УровеньВывода) Экспорт
	мСообщенияЛога.Добавить(Сообщение);
КонецПроцедуры

Процедура Закрыть() Экспорт
	мСообщенияЛога = Неопределено;
КонецПроцедуры

мСообщенияЛога = Новый Массив;