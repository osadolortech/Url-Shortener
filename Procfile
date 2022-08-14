release: python manage.py migrate
web gunicorn url_shortener.wsgi:application --log-file -