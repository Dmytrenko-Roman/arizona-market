from django.shortcuts import render

def market(request):
    return render(request, 'blog/post_list.html', {})
    