#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd evaluaciones_juan_manuel_miguel_alfaro_carlos_taquez
python manage.py collectstatic --no-input
python manage.py migrate
