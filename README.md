# portfolio
A portfolio python app using Django as a framework.

Work in progress....

1.
Setup the postgreSQL database.

```
-- Database:
-- https://docs.djangoproject.com/en/3.0/ref/settings/#databases

CREATE USER portfolio PASSWORD 'proj2023';
CREATE DATABASE portfoliodb OWNER portfolio;

```


2. Makemigrations

```
$ cd portfolio
$ python manage.py makemigrations
Migrations for 'profileapp':
  profileapp\migrations\0001_initial.py
    - Create model ProfileApp
Migrations for 'signupapp':
  signupapp\migrations\0001_initial.py
    - Create model LoginApp
    - Create model UserApp


```

3. Migrate

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, profileapp, sessions, signupapp
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying profileapp.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying signupapp.0001_initial... OK


```

4. Create Super User.

```
$ python manage.py createsuperuser
Username (leave blank to use 'YourUserName'): cool
Email address: cool@cool.org
Password:
Password (again):
Superuser created successfully.


```

5. Run the server.

```
$ py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 08, 2023 - 15:02:24
Django version 3.0.5, using settings 'portfolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```

6. Visit the site with your favourite web browser.


Enjoy...
