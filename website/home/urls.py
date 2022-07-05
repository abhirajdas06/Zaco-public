from home import views
from django.urls import include
from django.contrib import admin
from django.urls import path
 
urlpatterns = [
    path('', views.index,name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('technologies', views.technologies, name="technologies"),

]