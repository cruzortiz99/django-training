from django.urls import path, re_path
from app import views


urlpatterns = [
    re_path("^(?!api|admin|favicon|static)", views.IndexView.as_view()),
    path("api/home/", views.PageHomeView.as_view()),
    path("api/login/", views.PageLoginView.as_view()),
    path("api/sign-in/", views.PageSignInView.as_view()),
    path("api/adoption-center/", views.PageAdoptionCenterView.as_view()),
    path("api/pet-store/", views.PagePetStoreView.as_view()),
    path("api/user/", views.PageUser.as_view()),
]
