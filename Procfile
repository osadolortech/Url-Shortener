release: python manage.py migrate
python manage.py collectstatic --noinput;
web gunicorn url_shortener.wsgi:application --log-file -
