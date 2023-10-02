![Valorank image](https://github.com/danisimore/Valorank/raw/main/valorank_root/static/images/neon_valorank.jpg)

### ![USA Flag](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Flag_of_the_United_States_%281795-1818%29.svg/24px-Flag_of_the_United_States_%281795-1818%29.svg.png) *Welcome to the Valorank repository!*
This project is an online store for buying a boost of your account in the tactical online shooter Valorank. This is one of my Pet projects.
____
### Technologies that were used in the process of writing this web service:
- Python;
- Django;
- PostgreSQL;
- Docker;
- Gunicorn;
- Nginx;
- Git.

### Project functionality:
- Authentication with all features:
- Registration;
  - Authorization;
  - Mail confirmation;
  - Password Reset;
  - Password change;
  - Change of mail;
  - Authorization is not possible without email confirmation.
- Output of articles;
- Ability to go to the selected article;
- The user can select his current rank in the store and the rank to which he wants to buy a boost. Based on his choice, the product will be displayed;
- The form of contacting the support service. Queries are saved in the database.

____
### Users:
#### How does the user model work?
*The standard model has been redefined*.

For an ordinary user, only the is_verify field is important, which becomes true after confirming the mail. For employees there are fields `first_name`, `last_name`, `phone`, `discord`, `avatar`, `is_employee`, `position` and `mailbox`:
- `first_name', `last_name', `phone`, `discord`, `is_employee', `position' - required for employee identification;
- `avatar' is also suitable for identification. In addition, the avatars of the 3 best (chosen by you) boosters are displayed for users on the "About Us" page.
- `mailbox' - entered manually (example@gmail.com | --> example <-- @gmail.com ). Used in the 'support_service` application. Required to identify the employee processing the support request. It is also displayed on the "About us" page, under the boosters' avatar.

____
### Displayed content.
- #### *Displaying articles on the main page:*
  The main page displays the last 5 added articles. Sorted by `pk` in descending order in the file `valorank_root/main/views.py `.

- #### *Displaying bestsellers*
   The main page displays 3 products with the `is_bestseller` field set to `True`. The selection also takes place in the file `valorank_root/main/views.py `.

- #### *Displaying the best boosters*
    On the "About us" page, all boosters with the `is_best` field equal to `True` are displayed. File `valorank_root/main/views.py `.
   
- #### *Displaying all articles*
  All articles are displayed on the Articles page. The "Our Updates" section displays articles with the `is_update` field set to `True`. All the others are displayed in the "Articles & Useful Information" section.
- #### *Displaying a separate article*
  When you click on a separate article, its content and image are displayed. The rest of the articles are offered below. The selected article is excluded from the suggested ones.
    
____
### Installation and launch.
In order to clone this repository to your PC, you can use the command:

`git clone https://github.com/danisimore/Valorank.git`

#### *Launching the dev version*
- Clone the repository;
- Go to the `valorank_root` directory;
- Create a `.env.dev` file with variables:
``
  SECRET_KEY=YOUR_SECRET_KEY
  DEBUG=1
  DJANGO_ALLOWED_HOSTS='0.0.0.0 127.0.0.1'
  ```
- Create a file `.env.dev.db` with variables:
``
  POSTGRES=django.db.backends.postgresql_psycopg2
  POSTGRES_DB=postgres
  POSTGRES_USER=postgres
  POSTGRES_PASSWOD=postgres
  POSTGRES_HOST=db
  POSTGRES_PORT=5432
  ```
- Go to `valorank_root/valorank_config/settings.py `:
- Comment out these lines
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
    ``
- Uncomment:
``python
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ``
- Comment:
    ```python
    # CSRF_TRUSTED_ORIGINS = str(os.environ.get('CSRF_TRUSTED_ORIGINS')).split()
    ```
- Go to the `valorank_root` directory;
- Run the `docker-compose up -d --build` command;
- If migrations are not applied, you can use the command `docker-compose exec web python manage.py migrate`;
- Next, you can create a superuser with the command `docker-compose exec web python manage.py createsuperuser`;
- Profit! The dev version is available at `http://127.0.0.1:8000 /`.
#### *Launching the prod version*
- Clone the repository
- Go to the valorank_root directory
- Create a `.env.prod` file with variables:
``
  SECRET_KEY=YOUR_SECRET_KEY
  DEBUG=0
  DJANGO_ALLOWED_HOSTS='localhost your_domen'
  CSRF_TRUSTED_ORIGINS='http://127.0.0.1:1337 http://{your_domen.com}'

  EMAIL_HOST='smtp.yandex.ru'
  EMAIL_PORT=465
  EMAIL_USE_TLS=0
  EMAIL_USE_SSL=1
  EMAIL_HOST_USER=your_email
  EMAIL_HOST_PASSWORD=your_application_password

  ```
- Create a `.env.prod.db` file with variables:
    ```
    POSTGRES='django.db.backends.postgresql_psycopg2'
    POSTGRES_DB=your_db_name
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```
- Run the command `docker-compose -f docker-compose.prod.yml up -d --build`;
- Run the command `docker-compose -f docker-compose.prod.yml exec web python manage.py migrate`
- Run the command `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic`
- Run the command `docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser`
- Profit! If the deploy version is running on your machine, it is available at `http://localhost:1337 `. If the project is running on the server, then it is available at the server address.


### ![USA Flag](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/%D0%A4%D0%BB%D0%B0%D0%B3_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_%281%29.jpg/24px-%D0%A4%D0%BB%D0%B0%D0%B3_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8_%281%29.jpg) *Добро пожаловать в репозиторий Valorank!*
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
- Возможность перейти на выбраную статью;
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
  - Закомментировать данные строки
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
  CSRF_TRUSTED_ORIGINS='http://127.0.0.1:1337 http://{your_domen.com}'

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
