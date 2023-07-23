<h1 align="center"> Проект: сервис YaCut </h1>

___
<h4>Автор:</h4>

**Сластухин Александр** - студент Яндекс.Практикума Когорта 17+
https://github.com/last-ui

<h2>Краткое описание проекта</h2>
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

<h2>Подготовка проекта к запуску</h2>

- Установить и активировать виртуальное окружение

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

- Установить зависимости из файла requirements.txt

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

<h2>Запуск проекта</h2>

```shell
flask run
```

<h2>Примеры запросов</h2>

- POST-запрос на создание новой короткой ссылки:
```
localhost:8000/api/id/
Content-Type: application/json
{
  "url": "string",
  "custom_id": "string"
}
```

- Пример ответа от сервера:
```
{
  "url": "string",
  "short_link": "string"
}
```

-  GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору:
```
localhost:8000/api/id/1/
```

- Пример ответа от сервера:
```
{
  "url": "string"  
}
```

<h2>Используемые технологии</h2>

- [Python 3.10](https://www.python.org/downloads/release/python-10/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)