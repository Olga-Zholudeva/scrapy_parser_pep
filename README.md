# scrapy_parser_pep

## Данный проект осуществляет парсинг документации PEP на базе фреймворка Scrapy.

## Результат работы парсера:
- файл pep_ДатаВремя.csv содержит информацию по номерам, названиям и статусам PEP
- файл status_summary_ДатаВремя.csv содержит сводную информацию о количестве PEP в разрезе статусов и общем количестве PEP

## Технологии проекта:

- Python 3.7.9
- Scrapy 2.5.1

## Запуск проекта:

- [Клонируем репозиторий: git clone] (https://github.com/Olga-Zholudeva/scrapy_parser_pep)
- Cоздаем и активировируем виртуальное окружение: python3 -m venv env source env/bin/activate
- Устанавливаем зависимости из файла requirements.txt: pip install -r requirements.txt

## Получение результатов парсинга:

- scrapy crawl pep

## Проект выполнен:

Ольга Жолудева