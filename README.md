# python_autotests
Пример автотестов на pytest + requests

<h2>Автотесты на API проекта «Битва покемонов»</h2>

> **Статус проекта:**
> Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.ru/
> 
> 🟢 Поддерживается (активный) 

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Тест-кейсы, которые автоматизировали
* Создание покемона `POST /pokemons`
* Смена имени покемона `PUT /pokemons`
* Поймать покемона в покебол `POST /trainers/add_pokeball`
* Проверить ответ метода `GET /trainers`

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе приходит корректное поле id в json

## Детали реализации

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests
3. Параметризированные тесты с использованием декоратора

![image](https://raw.githubusercontent.com/AlexEr-QA/python_autotests/refs/heads/main/1.png)

## Локальный запуск тестов (из терминала)
1. Скачать проект
2. Перейти через терминал в директорию проекта
3. Выполнить команду:

Создаём виртуальное окружение внутри папки проекта.

``` markdown
PS> py -m venv venv\
```

``` markdown
PS> venv\Scripts\activate
(venv) PS>
```

4. Устанавливаем библиотеки

``` markdown
(venv) PS> python -m pip install requests
```

``` markdown
(venv) PS> python -m pip install pytest
```

Запускаем
``` markdown
pytest tests/test_pokemon.py
```

5. Ожидаемый результат: получим отчет о прохождении тестов.


## Автор

Ероскин Алексей ([@surra_gott](https://t.me/surra_gott))
