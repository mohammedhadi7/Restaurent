from django.shortcuts import render

def imp(request):
    return render(request,"drinks/imp.html")
  
def index(request):
    return render(request,"index.html")
