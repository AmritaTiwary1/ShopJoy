from django.contrib import admin
from django.urls import path

from home import views 
# I imported view so that by going to urls,it show context, views keep info about content
#It has info of all urls present in the project

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('buyPage',views.buyPage, name='buyPage')
    
]
