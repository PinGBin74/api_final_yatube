# API_FINAL_YATUBE

API_Final - законченная версия API для yatube c авторизацией по JWT токену.

**Стек:** Python 3.9, Django Rest Framework, SQLite

## Как запустить проект:

- **Клонировать репозиторий и перейти в него в командной строке:**
  ```sh
  git@github.com:PinGBin74/api_final_yatube.git

- **Создать и активировать виртуальное окружение:**
  ```sh
  python -m venv env
  source env/bin/activate

- **Установить зависимости из файла requirements.txt:**
  ```sh
  python -m pip install --upgrade pip
  pip install -r requirements.txt

- **Выполнить миграции:**
  ```sh
  python manage.py migrate

- **Запустить проект:**
  ```sh
  python manage.py runserver
