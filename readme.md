NEWBIE
----
$ python3 manage.py makemigrations
Migrations for 'S2':
  S2/migrations/0001_initial.py
    - Create model Adviser
    - Create model Branch
    - Create model Guarantor
    - Create model NavData
    - Create model NavFile
    - Create model Posterior
    - Create model Project
    - Add field Project to posterior
    - Add field Project to guarantor
    - Add field Project to adviser
$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: S2, admin, auth, contenttypes, sessions
Running migrations:
  Applying S2.0001_initial... OK
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
$ python3 manage.py createsuperuser
Username:
Email address:
Password: 
Password (again): 
Superuser created successfully.
$ python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
April 24, 2018 - 02:01:41
Django version 2.0.4, using settings 'newbie.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
