
# Readme

Данный репозиторий содержит выполненное тестовое задание на позицию "Python-разработчик (Django, DRF)"

## Текст задания

**Задача**: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: Django 2.2.10, Django REST framework.

Результат выполнения задачи:

- исходный код приложения в github (только на github, публичный репозиторий)
- инструкция по разворачиванию приложения (в docker или локально)
- документация по API

## Установка

1. Клонируем репозиторий с гитхаба

    ```bash
    git clone git@github.com/sotirr/test_task_for_fabrique_studio.git
    ```

2. устанавливаем docker и docker-compose

3. Запускаем докер контейнеры в фоновом режиме

    ```bash
    docker-compose up --build -d
    ```

4. Выполняем миграцию базы данных

    ```bash
    docker-compose run django_web /usr/local/bin/python manage.py migrate
    ```

5. Создаем администратора для django

    ```bash
    docker-compose run django_web /usr/local/bin/python manage.py createsuperuser
    ```

## Использование

Приложение запущенно и доступно на порту 8001

### Функционал для администратора системы

Функционал для администратора системы полностью реализован на админке django.

1. переходим на url http://127.0.0.1:8001/admin
2. авторизуемся под созданным нами администратором
3. переходим в раздел `polls/quizzes`
4. создаем, меняем удаляем опросники, вопросы в них и варианты ответов.

### Функционал для пользователей системы

Функционал для пользователей системы реализован в виде API.

Документация по API находится по адресу http://127.0.0.1:8001/swagger

## База данных

База данных в проекте используется postgres

Упрощена схема базы:

![bd_scheme](https://user-images.githubusercontent.com/47517203/106393569-b0512500-6419-11eb-83de-6051a4087b15.png)
