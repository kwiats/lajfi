#!/bin/bash
python3 manage.py migrate
python3 manage.py collectstatic --noinput
#celery -A core worker --loglevel=info &
#celery -A core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &
ln -s staticfiles easyTollApi/static
python3 -m http.server 9000 &
gunicorn --config gunicorn-cfg.py easyTollApi.wsgi