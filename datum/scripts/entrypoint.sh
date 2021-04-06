#!/bin/sh

set -e

# Wait for database to start
sleep 5

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput --full_name Admin --organisation Envector || true

# TODO: remove auto --py-autoreload in production
# uwsgi --http :9000 --master --enable-threads --module project.wsgi --py-autoreload 3
python manage.py runserver 0.0.0.0:8000