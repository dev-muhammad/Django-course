#!/bin/bash
set -euo pipefail
#python manage.py collectstatic --noinput
python manage.py migrate

python manage.py loaddata fixtures/*

python -u manage.py runserver 0.0.0.0:8000
