FROM python:3.8.3-alpine

# set work directory
WORKDIR /microservice

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . /microservice
RUN pip install -r requirements.txt
