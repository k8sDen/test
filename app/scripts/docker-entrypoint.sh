#!/bin/bash
python manage.py migrate --noinput
gunicorn app.wsgi:application --bind 0.0.0.0:8000