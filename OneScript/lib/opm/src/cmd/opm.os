///////////////////////////////////////////////////////////////////////////
//
// OneScript Package Manager
// Установщик пакетов для OneScript
// Выполняется, как os-приложение в командной строке:
//
// opm install my-package.ospx
//
////////////////////////////////////////////////////////////////////////

#Использовать "../core"
#Использовать "."
#Использовать cli

Перем ЭтоWindows;

///////////////////////////////////////////////////////////////////////////////

Процедура ВыполнитьПриложение()

    Приложение = Новый КонсольноеПриложение("opm", НСтр("ru='Пакетный менеджер для OneScript';en='Package manager for OneScript'"));
    Приложение.Версия("v version", КонстантыOpm.ВерсияПродукта);

    Приложение.ДобавитьКоманду("a app", НСтр("ru='Создать ';en='Create '") + ?(ЭтоWindows, "bat", "sh") + НСтр("ru='-файл для запуска скрипта в указанном каталоге';en='-file to run the script in the specified directory'"), Новый КомандаOpm_App);
    Приложение.ДобавитьКоманду("b build", НСтр("ru='Собрать пакет из исходников';en='Build a package from source'"), Новый КомандаOpm_Build);
    Приложение.ДобавитьКоманду("c config", НСтр("ru='Задать пользовательские настройки';en='Configure user settings'"), Новый КомандаOpm_Config);
    Приложение.ДобавитьКоманду("i install", НСтр("ru='Выполнить установку пакета. 
                                        |                Если указано имя пакета, происходит установка из хаба или из файла. 
                                        |                В обратном случае устанавливаются зависимости текущего пакета по файлу packagedef.'
                                        |en='Install the package.
                                        |                If the package name is specified, the installation is performed from the hub or from the file. 
                                        |                Otherwise, the dependencies of the current package are set using the packagedef file.'"),
                                        Новый КомандаOpm_Install);
    Приложение.ДобавитьКоманду("ls list", НСтр("ru='Вывести список пакетов';en='Show list of packages'"), Новый КомандаOpm_List);
    Приложение.ДобавитьКоманду("pre prepare", НСтр("ru='Подготовить новый каталог разрабатываемого пакета';en='Prepare a new catalog for the development package'"), Новый КомандаOpm_Prepare);
    Приложение.ДобавитьКоманду("p push", НСтр("ru='Отправить пакет в хаб пакетов';en='Send the package to the package hub'"), Новый КомандаOpm_Push);
    Приложение.ДобавитьКоманду("r run", НСтр("ru='Выполнить произвольную задачу';en='Run a task'"), Новый КомандаOpm_Run);
    Приложение.ДобавитьКоманду("test", НСтр("ru='Выполнить тестирование проекта';en='Run project testing'"), Новый КомандаOpm_Test);
    Приложение.ДобавитьКоманду("u update",  НСтр("ru='Обновить пакет';en='Update package'"), Новый КомандаOpm_Update);
    Приложение.ДобавитьКоманду("version", НСтр("ru='Вывести версию продукта';en='show application version'"), Новый КомандаOpm_Version);
   
    Приложение.Запустить(АргументыКоманднойСтроки);

КонецПроцедуры

///////////////////////////////////////////////////////

СистемнаяИнформация = Новый СистемнаяИнформация;
ЭтоWindows = Найти(НРег(СистемнаяИнформация.ВерсияОС), "windows") > 0;

Попытка

    ВыполнитьПриложение();

    ВременныеФайлы.Удалить();

    ЗавершитьРаботу(0);

Исключение
    Сообщить(ОписаниеОшибки());

    ВременныеФайлы.Удалить();

    ЗавершитьРаботу(1);
КонецПопытки;