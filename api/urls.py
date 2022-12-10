from django.urls import path
from api import views


urlpatterns = [
    path('template/', views.index),
    path('name/', views.say_hello),
]
