from django.shortcuts import render

def market(request):
    return render(request, 'market/market.html', {})
