from django.apps import AppConfig
from django.urls import path
from . import views

urlpatterns=[
    path('',views.ph_login),
    path('phnbook',views.phnbook),
    path('register',views.register),
    
    
    
]