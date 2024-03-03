
from django.contrib import admin
from django.urls import path , include

#for changing text of admin page = https://books.agiliq.com/projects/django-admin-cookbook/en/latest/change_text.html#:~:text=How%20to%20change%20%E2%80%98Django%20administration%E2%80%99%20text%3F%20%C2%B6%201,and%20is%20set%20to%20%E2%80%9CDjango%20site%20admin%E2%80%9D%20
#i went to this link and copy the code and make some changes like "amrita ice cream"
admin.site.site_header = "Amrita ShopJoy Admin"
admin.site.site_title = "ShopJoy Admin Portal"
admin.site.index_title = "Welcome to MY SHOP "


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('home.urls'))
]

