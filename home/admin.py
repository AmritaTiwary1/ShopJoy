#username : admin password : admin
# i got error while running  http://127.0.0.1:8000/admin , saying operational error so run python manager.py makemigrations then python manager.py migrate in terminal then runserver
#it will create a table for admin username & password and hence will open the http://127.0.0.1:8000/admin
from django.contrib import admin
from home.models import Contact
# Register your models here
admin.site.register(Contact)
