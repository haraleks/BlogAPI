#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ ! -d 'logs' ]; then
    mkdir 'logs'
fi

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"
