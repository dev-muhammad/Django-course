#!/bin/bash
set -euo pipefail

python manage.py collectstatic --noinput
python manage.py migrate

python manage.py loaddata fixtures/*
gunicorn backend.wsgi:application -b 0.0.0.0:8001 --threads 2 --workers 4 --worker-class gthread --log-level debug --error-logfile /log/gunicorn_error.log
