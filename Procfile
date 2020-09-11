web: gunicorn hospitalMIS.wsgi:application --log-file -
release: python manage.py makemigrations && python manage.py migrate