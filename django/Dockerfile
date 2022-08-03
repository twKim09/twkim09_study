FROM python:3.9.6-alpine3.14

COPY ./requirement1.txt /requirement1.txt
COPY ./django_swagger /django_swagger


RUN apk add build-base gcc python3-dev musl-dev libffi-dev openssl-dev curl vim
RUN python3 -m pip install --upgrade pip && pip install --upgrade setuptools && pip install -r /requirement1.txt

RUN ["chmod","+x","/django_swagger"]
EXPOSE 8000
WORKDIR /django_swagger/
ENTRYPOINT ["gunicorn","--bind","0:8000","django_swagger.wsgi:application"]

