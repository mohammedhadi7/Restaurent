from django.shortcuts import render

# Create your views here

def index(request):
    return render(request,"index.html")

def imp(request):
    return render(request,"biryani/welcome.html")

