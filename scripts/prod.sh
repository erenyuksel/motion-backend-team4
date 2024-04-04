#!/bin/bash
python -c "import time; time.sleep(3)" # Wait 3 seconds for postgres service to boot up
python manage.py collectstatic --no-input
python manage.py migrate
gunicorn -w 4 -b 0.0.0.0:8000 motion_project.wsgi:application
