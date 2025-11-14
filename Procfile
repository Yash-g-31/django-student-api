release: python manage.py migrate --noinput
web: python manage.py collectstatic --noinput && gunicorn dev_portal.wsgi:application