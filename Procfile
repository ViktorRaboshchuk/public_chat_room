release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn --pythonpath django_chat_room django_chat_room.wsgi --log-file -
