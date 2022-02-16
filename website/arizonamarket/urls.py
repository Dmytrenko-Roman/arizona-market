from django.urls import path

from . import views

urlpatterns = [
    path("", views.MarketPageView.as_view(), name="market"),
    path("sell", views.CarSellView.as_view(), name="sell"),
    path("search", views.SearchView.as_view(), name="search"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.Login.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
]
