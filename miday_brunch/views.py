from django.shortcuts import render

from miday_brunch.models import Meal

def index(request):
    return render(request,"index.html")

def brunch(request):
    data=Meal.objects.all()
    return render(request,"midaybrunch/web.html",{"midaybrunch":data})
    
def mbrunch(request):
    return render(request,"midaybrunch/add_brunch.html")

