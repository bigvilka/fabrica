FROM python:3.8
WORKDIR /app
COPY ./requirements.txt /app
COPY . /app
RUN pip install -r requirements.txt
RUN django-admin manage.py runserver