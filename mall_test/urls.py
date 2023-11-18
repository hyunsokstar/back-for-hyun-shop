from django.urls import path
from . import views

# prefix
# 127.0.0.1:8000/accounts/
urlpatterns = [
    path("payment/new/", views.payment_new, name="payment_new"),
    path("hello/", views.HelloWorldView.as_view(), name="hello-world"),
]
