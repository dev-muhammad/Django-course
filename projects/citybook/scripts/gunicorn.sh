#!/bin/bash
set -euo pipefail

# python manage.py collectstatic --noinput
python manage.py migrate

python manage.py loaddata fixtures/*
gunicorn config.wsgi:application -b 0.0.0.0:8000 --threads 2 --workers 4 --worker-class gthread
