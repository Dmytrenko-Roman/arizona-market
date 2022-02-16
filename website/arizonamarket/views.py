from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView, RedirectView

from .models import Car, CustomUser
from .forms import CustomUserCreationForm, CarSellForm


class MarketPageView(TemplateView):

    template_name = "market/market.html"

    def get_context_data(self, **kwargs):
        context = super(MarketPageView, self).get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context


def market_post(request):
    msg = ""

    if request.method == "POST":
        form = CarSellForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = CustomUser.objects.get(pk=request.user.id)
            car.save()
            msg = "Successfully sold car!"
        else:
            msg = "Unsuccessful. Invalid information."

    form = CarSellForm()

    context = {
        "form": form,
        "message": msg,
    }

    return render(request=request, template_name="market/sell.html", context=context)


def register_request(request):
    msg = ""

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            msg = "Registration successful."
            return redirect("market")
        msg = "Unsuccessful registration. Invalid information."

    form = CustomUserCreationForm()

    context = {
        "register_form": form,
        "message": msg,
    }

    return render(
        request=request, template_name="market/register.html", context=context
    )


def login_request(request):
    msg = ""

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                msg = f"You are now logged in as {username}."
                return redirect("market")
            else:
                msg = "Invalid username or password."
        else:
            msg = "Invalid username or password."

    form = AuthenticationForm()

    context = {
        "login_form": form,
        "message": msg,
    }

    return render(request=request, template_name="market/login.html", context=context)


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'market'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)
