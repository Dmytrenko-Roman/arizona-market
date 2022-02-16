from django.urls import path

from . import views

urlpatterns = [
    path("", views.MarketPageView.as_view(), name="market"),
    path("sell", views.CarSellView.as_view(), name="sell"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
]
