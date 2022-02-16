from django.urls import path

from . import views

urlpatterns = [
    path("", views.market_get, name="market"),
    path("sell", views.market_post, name="sell"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]
