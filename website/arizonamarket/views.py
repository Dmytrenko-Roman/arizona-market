from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, CreateView, RedirectView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .models import Car, CustomUser
from .forms import CustomUserCreationForm, CarSellForm


class MarketPage(ListView):
    model = Car
    template_name = "market/market.html"
    context_object_name = "cars"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['highlights'] = {
            'market': 'active',
            'sell': '',
            'mycars': '',
            'login': '',
            'register': '',
        }
        return context


class SellPage(CreateView):
    template_name = "market/sell.html"
    form_class = CarSellForm
    success_url = "/sell"

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = CustomUser.objects.get(pk=self.request.user.id)
        car.save()
        return super(SellPage, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['highlights'] = {
            'market': '',
            'sell': 'active',
            'mycars': '',
            'login': '',
            'register': '',
        }
        return context


class SearchPage(ListView):
    model = Car
    template_name = "market/market.html"
    context_object_name = "cars"

    def get_queryset(self):
        query = self.request.GET.get("q")
        cars = Car.objects.filter(model__icontains=query)
        return cars


class MyCarsPage(ListView):
    model = Car
    template_name = "market/mycars.html"
    context_object_name = "cars"

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user.id)


class CarUpdate(UpdateView):
    model = Car
    fields = [
        "model",
        "twinturbo",
        "mileage",
        "price",
    ]
    success_url = "/mycars"
    template_name = "market/update.html"


class Register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "market/register.html"


class Login(LoginView):
    authentication_form = AuthenticationForm
    form_class = AuthenticationForm
    template_name = "market/login.html"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class Logout(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "market"

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(Logout, self).get_redirect_url(*args, **kwargs)
