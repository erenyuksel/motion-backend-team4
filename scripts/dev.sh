python -c "import time; time.sleep(3)" # Wait 3 seconds for postgres service to boot up
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0:8000
