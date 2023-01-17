![Valorank image](https://github.com/danisimore/Valorank/raw/main/valorank_root/static/images/neon_valorank.jpg)

### *Добро пожаловать в репозиторий Valorank!*
Данный проект представляет собой онлайн-магазин для покупки буста своего аккаунта в тактическом онлайн шутере Valorank. Это один из моих Pet-проектов.
____
### Технологии, которые были использованы в процессе написания данного веб-сервиса:
- Python;
- Django;
- PostgreSQL;
- Docker;
- Gunicorn;
- Nginx;
- Git.

### Функционал проекта:
- Аутентификация со всеми возможностями:
  - Регистрация;
  - Авторизция;
  - Подтверждение почты;
  - Сброс пароля;
  - Смена пароля;
  - Смена почты;
  - Авторизация невозможна без подтверждения почты.
- Вывод статей;
- Возможность перейти на выбрнную статью;
- Возможность пользователем выбрать в магазине его текущий ранг и ранг, до которого он хочет купить буст. На основе его выбора будет выведен товар;
- Форма обращения в службу поддержки. Запросы сохраняются в БД.

____
### Пользователи:
#### Как устроена модель пользователя?
*Стандартная модель была переопределена*.

Для обычного юзера важно лишь поле is_verify, которое становится истинным, после подтверждения почты. Для сотрудников имеются поля `first_name`, `last_name`, `phone`, `discord`, `avatar`, `is_employee`, `position` и `mailbox`:
- `first_name`, `last_name`, `phone`, `discord`, `is_employee`, `position` - необходимы для идентификации сотрудника;
- `avatar` - также нобходим для идентификации. Помимо этого, аватары 3-х лучших (выбранных вами) бустеров выводятся для пользователей на странице "О нас".
- `mailbox` - вводится вручную (example@gmail.com | --> example <-- @gmail.com). Используется в приложении `support_service`. Необходим для идентификации сотрудника, обрабатывающего запрос в службу поддержки. Так же выводится на странице "О нас", под аватаркой бустеров.

____
### Отображаемый контент.
- #### *Отображение статей на главной странице:*
  На главной странице отображаются последние 5 добавленных статей. Сортируются по `pk` в порядке убывания в файле `valorank_root/main/views.py`.

- #### *Отображение бестселлеров*
   На главной странице отображаются 3 товара, у которых поле `is_bestseller` равно `True`. Выборка происходит также в файле           `valorank_root/main/views.py`.

- #### *Отображение лучших бустеров*
    На странице "О нас" выводятся все бустеры, у которых поле `is_best` равно `True`. Файл `valorank_root/main/views.py`.
   
- #### *Отображение всех статей*
  На странице "Статьи" выводятся все статьи. В разделе "Наши обновления" выводятся статьи, у которых поле `is_update` равно `True`. Все остальные выводятся в разделе "Статьи & Полезная информация".
- #### *Отображение отдельной статьи*
  При переходе на отдельную статью отображается ее контент и изображение. Снизу предлагаются остальные статьи. Выбранная статья исключенна из предложенных.
    
____
### Установка и запуск.
Для того чтобы склонировать данный репозиторий к себе на ПК, вы можете воспользоваться командой:

`git clone https://github.com/danisimore/Valorank.git`

#### *Запуск dev версии*
- Склонировать репозиторий;
- Перейти в директорию `valorank_root`;
- Создать файл `.env.dev` с переменными:
  ```
  SECRET_KEY=YOUR_SECRET_KEY
  DEBUG=1
  DJANGO_ALLOWED_HOSTS='0.0.0.0 127.0.0.1'
  ```
- Создать файл `.env.dev.db` с переменными:
  ```
  POSTGRES=django.db.backends.postgresql_psycopg2
  POSTGRES_DB=postgres
  POSTGRES_USER=postgres
  POSTGRES_PASSWOD=postgres
  POSTGRES_HOST=db
  POSTGRES_PORT=5432
  ```
- Прейти в `valorank_root/valorank_config/settings.py`:
  - Заккоментировать данные строки
    ```python
    # For deploy version
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = os.environ.get('EMAIL_HOST')
    # EMAIL_PORT = os.environ.get('EMAIL_PORT')
    # EMAIL_USE_TLS = bool(int(os.environ.get('EMAIL_USE_TLS')))
    # EMAIL_USE_SSL = bool(int(os.environ.get('EMAIL_USE_SSL')))
    # EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    # EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    # DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    ```
  - Раскомментировать: 
    ```python
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ```
  - Закомментировать:
    ```python
    # CSRF_TRUSTED_ORIGINS = str(os.environ.get('CSRF_TRUSTED_ORIGINS')).split()
    ```
- Перейти в директорию `valorank_root`;
- Запустить команду `docker-compose up -d --build`;
- Если миграции не применились, вы можете воспользоваться командой `docker-compose exec web python manage.py migrate`;
- Далее вы можете создать суперюзера командой `docker-compose exec web python manage.py createsuperuser`;
- Profit! Dev версия доступна по адресу `http://127.0.0.1:8000/`.
#### *Запуск prod версии*
- Склонировать репозиторий
- Перейти в директорию valorank_root
- Создать файл `.env.prod` с переменными:
  ```
  SECRET_KEY=YOUR_SECRET_KEY
  DEBUG=0
  DJANGO_ALLOWED_HOSTS='localhost your_domen'
  CSRF_TRUSTED_ORIGINS='http://localhost:1337 http://{your_domen.com}'

  EMAIL_HOST='smtp.yandex.ru'
  EMAIL_PORT=465
  EMAIL_USE_TLS=0
  EMAIL_USE_SSL=1
  EMAIL_HOST_USER=your_email
  EMAIL_HOST_PASSWORD=your_application_password

  ```
- Создать файл `.env.prod.db` с переменными:
    ```
    POSTGRES='django.db.backends.postgresql_psycopg2'
    POSTGRES_DB=your_db_name
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```
- Запустить команду `docker-compose -f docker-compose.prod.yml up -d --build`;
- Запустить команду `docker-compose -f docker-compose.prod.yml exec web python manage.py migrate`
- Запустить команду `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic`
- Запустить команду `docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser`
- Profit! Если deploy версия запущена на вашей машине она доступна по адресу `http://localhost:1337`. Если проект запущен на сервере, то он доступен по адресу сервера.
