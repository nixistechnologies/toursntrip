from django.shortcuts import render
from app.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def list_page(request):
    packages = Package.objects.all()
    return render(request,'listpage.html',{"packages":packages})