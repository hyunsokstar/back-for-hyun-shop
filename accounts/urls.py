from django.urls import path
from . import views


urlpatterns = [
    # URL 패턴들을 여기에 추가
    path("test", views.template_test),
    path("login", views.LoginView.as_view()),
    path("logout", views.LogoutView.as_view()),
    path("check-login", views.CheckViewForLogin.as_view()),
]
