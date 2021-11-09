pip3 install virtualenv
virtualenv -p python3 env
source env/bin/activate

pip install django

# Getting started
`django-admin startproject my_project`
`cd my_project`
`python manage.py startapp my_app`
`python manage.py runserver`
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py createsuperuser`
`python manage.py sqlmigrate diary 0001_initial`

- For printing on console:

`python -u manage.py runserver `

- Recreate an environment from `requirements.txt`
`virtualenv env`
`source env/bin/activate`
`pip install -r requirements.txt`

- To see output from `print` statements in console: `python -u manage.py runserver`

- Prepare static files to serve from production server:
`python manage.py collectstatic`