from django.urls import path

from . import views

urlpatterns = [
    path("", views.MarketPageView.as_view(), name="market"),
    path("sell", views.market_post, name="sell"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
]
