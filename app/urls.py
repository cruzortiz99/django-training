from django.urls import path, re_path
from app import views


urlpatterns = [
    re_path("^(?!api)", views.index),
    path("api/home/", views.page_home),
    path("api/page-1/", views.page_one),
    path("api/page-2/", views.page_two),
    path("api/page-3/", views.page_three),
]
