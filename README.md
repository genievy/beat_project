# beat_project
"""
Техническое задание.
	Браузер Chrome и Firefox		
			
Шаг	Действие	                                       ОР	
1	Открыть в браузере ссылку https://demoqa.com/	       Сайт https://demoqa.com/ открыт	
2	Нажать кнопку Elements	                               Открыта страница Elements	
3	В раскрытом меню справа кликнуть лкм Check Box	       Открыта страница Check Box	
4	Раскрыть директорию Home. 	                       Директория Home раскрыта	
5	Раскрыть директорию Downloads 	                       Директория Downloads раскрыта	
6	Выбрать чекбокс Word File.doc	                       "Чекбокс файла Word File.doc выбран. 
                                                                Появилось сообщение ""You have selected:wordFile"""	
			


Реализация.

Запуск тестов (в корне проекта):

 pytest -s -v tests\test_elements.py
 
Запуск проекта с генерацией отчета в allure:

  pytest -s -v tests\test_elements.py --alluredir=C:\beat_project\tests\reports

Для просмотра отчета в браузере:

  allure serve tests\reports
  


Общее описание структуры проекта и подготовкеи окружения.

 ОС Windows 7, python 3.8, браузер Chrome,путь к исполняемому файлу  chromdriver добавлен в в системные переменные.

Подготовка.

1. Создаю папку проекта:
	C:\beat_project
2. Создаю окружение. Можно через настройки IDE или в терминале, или непосредственно в командной строке операционной системы:
>cd C:\beat_project
> python -m venv venv
3. Активирую venv:
	> venv\Scripts\activate
   и закрываем интерпретатор командной строки.

Переходим к разработке проекта.
a) Установка библиотек.

1. Открываем проект в среде разработки (я использую PyCharm).
2. Устанавливаем необходимые библиотеки:
	- selenium:
		(venv) C:\beat_project>pip install selenium
	- pytest:
		(venv) C:\beat_project>pip install pytest
	- allure:
		(venv) C:\beat_project>pip install allure-pytest
3. Создаем файл requirements.txt (список библиотек с указанием актуальных версий). В дальнейшем можем установить эти библиотеки одной командой:
	(venv) C:\beat_project>pip install –r requirements.txt

b) Структура проекта.

1. Создаю файл conftest.py, в нем пропишем функцию, которую pytest будет выполнять перед каждым запуском моих тестов.
2. Структура:
	>data
		>data.py
	>locators
		>elements_locators.py
	>pages
		>base_objects.py
		>elements_page.py
	>tests
		>test_elements.py
	>venv
	conftest.py
	requirements.txt
"""
