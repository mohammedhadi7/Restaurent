from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def brunch(request):
    return render(request,"midaybrunch/web.html")

