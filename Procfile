web: gunicorn peerreviewsite.wsgi
release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
