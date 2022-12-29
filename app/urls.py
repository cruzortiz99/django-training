from django.urls import path, re_path
from app import views


urlpatterns = [
    re_path("^(?!api|admin)", views.IndexView.as_view()),
    path("api/home/", views.PageHomeView.as_view()),
    path("api/page-1/", views.PageOneView.as_view()),
    path("api/page-2/", views.PageTwoView.as_view()),
    path("api/page-3/", views.PageThree.as_view()),
]
