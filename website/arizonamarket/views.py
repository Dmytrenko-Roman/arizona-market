from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy

from .models import Car, CustomUser
from .forms import CustomUserCreationForm, CarSellForm


class MarketPageView(TemplateView):

    template_name = "market/market.html"

    def get_context_data(self, **kwargs):
        context = super(MarketPageView, self).get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context


class CarSellView(FormView):
    template_name = 'market/sell.html'
    form_class = CarSellForm
    success_url = '/'

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = CustomUser.objects.get(pk=self.request.user.id)
        car.save()
        return super(CarSellView, self).form_valid(car)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'market/register.html'


# def register_request(request):
#     msg = ""

#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             msg = "Registration successful."
#             return redirect("market")
#         msg = "Unsuccessful registration. Invalid information."

#     form = CustomUserCreationForm()

#     context = {
#         "register_form": form,
#         "message": msg,
#     }

#     return render(
#         request=request, template_name="market/register.html", context=context
#     )


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
