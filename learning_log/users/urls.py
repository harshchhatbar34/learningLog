"""Defining urls patttern for users"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns =[
    #Low in url.
    path('', include('django.contrib.auth.urls')),

    #Logout url
    path('logout', views.logout_view, name='logout'),

    #Registrasion url
   path('register/', views.register, name='register'),
]


