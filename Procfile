release: python  django_chat_room.manage.py makemigrations
release: python django_chat_room.manage.py migrate
web: gunicorn --pythonpath django_chat_room django_chat_room.wsgi --log-file -
