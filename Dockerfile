FROM python:3.8


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/django/user-registar/

COPY ./requirements.txt /usr/django/requirements.txt
RUN pip install -r /usr/django/requirements.txt

COPY . /usr/django/user-registar/

# EXPOSE 8000
# CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']