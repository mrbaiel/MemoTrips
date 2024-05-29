# MemoTrips

MemoTrips - это веб-приложение для сохранения ваших воспоминаний о посещенных местах, где вы можете отмечать их на карте и оставлять комментарии.


### Системные требования

- Python 3.6 или выше
- Django 3.0 или выше

### Шаги установки

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/ваш-пользователь/ваш-репозиторий.git
    cd ваш-репозиторий
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции базы данных:
    ```bash
    python manage.py migrate
    ```

5. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

6. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000` для доступа к приложению.

## Использование

### Функции

- Регистрация и вход пользователей.
- Добавление, редактирование и удаление заметок.
- Отображение заметок на карте.
- Сохранение комментариев к местам.

### Основные URL-адреса

- Главная страница: `http://127.0.0.1:8000`
- Вход: `http://127.0.0.1:8000/login`
- Выход: `http://127.0.0.1:8000/logout`
- Добавить заметку: `http://127.0.0.1:8000/notes/add`
- Редактировать заметку: `http://127.0.0.1:8000/notes/<int:pk>/edit`
- Удалить заметку: `http://127.0.0.1:8000/notes/<int:pk>/delete`

### Примеры использования

После входа в систему вы сможете добавлять новые заметки, редактировать существующие и удалять ненужные. Все ваши заметки будут отображены на главной странице.
### Скриншоты веб-приложения
Страница входа
![image](https://github.com/mrbaiel/MemoTrips/assets/151663535/30aecda6-ef43-44aa-ab15-b014b2388530)

Основная страница
![image](https://github.com/mrbaiel/MemoTrips/assets/151663535/7b2f7f20-c15c-493a-ab06-8726b239c124)

Страница добавления запися
![image](https://github.com/mrbaiel/MemoTrips/assets/151663535/4196099a-3758-4cd2-9369-e828cd3902ef)

Страница редактирования
![image](https://github.com/mrbaiel/MemoTrips/assets/151663535/9d9e79b6-6d94-4ed6-97a2-2393869ff82c)
