from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def tiffins(request):
    return render(request,'tiffins/tiffins.html')
