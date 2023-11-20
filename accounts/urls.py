from django.urls import path
from . import views


urlpatterns = [
    path("user", views.ListViewForUser.as_view()),
    path("user/create", views.CreateViewForUser.as_view()),
    path("test", views.template_test),
    path("login", views.LoginView.as_view()),
    path("logout", views.LogoutView.as_view()),
    path("check-login", views.CheckViewForLogin.as_view()),
]
