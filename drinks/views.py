from django.shortcuts import render


def index(request):
    return render(request,"index.html")
    
def aaa(request):
    return render(request,"drinks/drinks.html")
  
