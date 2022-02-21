from django.urls import path

from . import views

urlpatterns = [
    path("", views.MarketPage.as_view(), name="market"),
    path("sell", views.SellPage.as_view(), name="sell"),
    path("<pk>/update", views.CarUpdate.as_view(), name="update"),
    path("mycars", views.MyCarsPage.as_view(), name="mycars"),
    path("search", views.SearchPage.as_view(), name="search"),
    path("register", views.Register.as_view(), name="register"),
    path("login", views.Login.as_view(), name="login"),
    path("logout", views.Logout.as_view(), name="logout"),
]
