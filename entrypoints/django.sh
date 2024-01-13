#!/bin/bash -x
echo "Django service is running ..."
python manage.py collectstatic --noinput --settings=uav_rental.settings_prod &&
python manage.py migrate --noinput --settings=uav_rental.settings_prod &&
python manage.py docker_create_superuser --settings=uav_rental.settings_prod &&
python manage.py runserver 0.0.0.0:8000 --settings=uav_rental.settings_prod &&
gunicorn uav_rental.wsgi:application --bind 0.0.0.0:8000 --timeout 600 --workers=3 --threads=3 --worker-connections=1000

exec "$@"
