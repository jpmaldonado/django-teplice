pip3 install virtualenv
virtualenv -p python3 env
source env/bin/activate

virtualenv -p python3 .
source bin/activate

pip install django

# Getting started
django-admin startproject my_project
cd my_project
python manage.py startapp my_app
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py sqlmigrate diary 0001_initial