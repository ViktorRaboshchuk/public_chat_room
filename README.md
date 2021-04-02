# chat_room

**Django Rest Framework public chat room application, where unauthenticated users can leave messages.**

*Link to Heroku project:* 

https://django-chat-room-api.herokuapp.com/swagger/

Steps to deploy project to Heroku:
- heroku create django-main-api-chat
- git init
- heroku git:remote -a django-main-api-chat
- git add -A
- git commit -am "commit message"
- git push
- heroku buildpacks:set heroku/python
- heroku config:set     DISABLE_COLLECTSTATIC=1
- git push heroku master
- heroku run python manage.py migrate
- heroku ps:scale web=1 (my deployment didn't work without it)
- heroku open
