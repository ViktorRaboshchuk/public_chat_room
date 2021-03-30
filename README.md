# chat_room

heroku create django-main-api-chat
git init
heroku git:remote -a django-main-api-chat
git add -A
git commit -am "commit message"
heroku buildpacks:set heroku/python
