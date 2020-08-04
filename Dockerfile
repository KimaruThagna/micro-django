FROM python:3.8.3-alpine

# set work directory
WORKDIR /microservice

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . /microservice
RUN pip install -r requirements.txt
CMD ["/bin/bash", "./entrypoint.sh"]
#ENTRYPOINT["entrypoint.sh"] alternative to CMD bin/bash
