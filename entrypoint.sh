#!/bin/bash
set -e

set -a
source /run/secrets/app_secrets
set +a

export DEBUG=0


python manage.py makemigrations --noinput

python manage.py migrate --noinput

python manage.py createsuperuser --noinput || true

python manage.py collectstatic --noinput

exec python -m gunicorn --bind "0.0.0.0:8000" --workers "3" where_is_my_pal.wsgi:application
