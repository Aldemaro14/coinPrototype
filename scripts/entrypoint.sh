#!/bin/sh

#If a command doesn work, it won't continue, used for debuggin apps
set -e

#Put all the static files in the static directory, Nginx will serve it and not uwsgi
python manage.py collectstatic --noinput

#Change app.wsgi for your project name + .wsgi
uwsgi --socket :8000 --master --enable-threads --module app.wsgi