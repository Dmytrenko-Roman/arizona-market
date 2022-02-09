from django.shortcuts import render
from .models import Car

def market(request):
    cars = Car.objects.all()
    return render(request, 'market/market.html', {'cars': cars})
