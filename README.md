# Installation

```bash
1. python -m venv .venv
2. .venv/Scripts/Activate
3. pip install -r requirements.txt
```

## Django
```bash
django-admin startproject project_name
cd project_name
create db_settings.conf in project folder and change config_parser.py
django-admin startapp project_app
python manage.py runserver
```
## DB

```bash
4. python manage.py makemigrations app_name
5. python manage.py migrate ( to create the schema )
6. python manage.py createsuperuser ( then go to host/admin page )
```

## Git

```bash
(once) git clone git@github.com:Dim41k3/lab7_9.git
git checkout -b develop
git add .
git commit -m "description"
git push origin develop
```
