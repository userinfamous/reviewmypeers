web: gunicorn peerreviewsite.wsgi
release: python manage.py makemigrations --noinput && python manage.py migrate && python manage.py collectstatic --noinput
