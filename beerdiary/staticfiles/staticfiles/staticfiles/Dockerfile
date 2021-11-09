FROM python:3.9

# Avoid writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# make console not buffered by Docker
ENV PYTHONUNBUFFERED 1

# Switch from DEBUG to PROD
ENV DEBUG 0

WORKDIR /code
COPY . /code/

# If you want to have a virtual environment (not necessary)
# RUN pip install virtualenv
# RUN virtualenv env
# RUN source env/bin/activate

RUN pip install -r requirements.txt
 
