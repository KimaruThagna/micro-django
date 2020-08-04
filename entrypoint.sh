#!/bin/sh

if [ "$ENGINE" = "django.db.backends.postgresql" ]; then
  echo "Initializing postgres db..."

  while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
  done

  echo "postgres database has initialized successfully"
fi

exec "$@"
