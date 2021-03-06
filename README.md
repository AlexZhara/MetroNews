# MetroNews

## Задание
> Написать **API**, которое получает новости за заданный период из базы,
и **парсер** который каждые 10 минут парсит новости
с сайта [https://mosmetro.ru/news](https://mosmetro.ru/news)
(достаточно будет просто взять те новости что есть при первой загрузке)
и сохраняет в базу с меткой когда эти новости спаршены,
>
> пример метода
> /metro/news?day=5
>
> в качестве ответа вернуть JSON новости которые опубликованы за последний 5 дней (включительно)
> заголовок
> url картинки
> дата публикации (YYYY-mm-dd)
>
> что использовать
> flask, docker + любая база

## Инструкция по запуску
1. Клонировать репозиторий и перейти в корневую папку `MetroNews` в терминале
2. Установить виртуальную среду: `$ python3 -m venv env` (или `python`, если там Python 3)
3. Активировать виртуальную среду.
    - На macOS: `$ source env/bin/activate`
    - На Windows: `$ env\Scripts\activate`
4. Установить requirements: `$ pip install -r requirements.txt`
5. Из корневой папки ввести команду `$ python parser`
    - Создастся база данных, и запустится `schedule` процесс.
6. Открыть новое окно терминала, перейти в корневую папку `MetroNews`, активировать виртуальную среду.
7. Из корневой папки ввести команду `$ flask run`
    - Запустится сервер на `localhost:5000`

Роут работает как в описании задачи: `localhost:5000/metro/news`

Если без аргументов, то выдаст все записи в БД. 

Если есть аргумент `?day=int`, то выдаст новости, опубликованные за последние `day` дней.
