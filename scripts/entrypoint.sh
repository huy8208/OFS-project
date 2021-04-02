#!/bin/sh

#Stop if run into any errors
set -e

#Collect static files
echo "Collect static files."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations."
python manage.py migrate

# Start server
uwsgi --socket :8000 --master --enable-threads --module project_settings.wsgi