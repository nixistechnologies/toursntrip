from django.shortcuts import render
from django.http.response import HttpResponseRedirect,JsonResponse
from app.models import *
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request,'index.html')

def list_page(request):
    packages = Package.objects.all()
    npackage = len(packages)
    paginator = Paginator(packages, 5)
    page_number = request.GET.get('page')
    packages = paginator.get_page(page_number)

    return render(request,'listpage.html',{"packages":packages,"count":npackage})

def submitQuery(request):
    data = request.POST
    print(data["packid"])
    
    print(data)
    return JsonResponse(data)

def detailPage(request,package):
    pack_id = package.split("-")[-1]
    print(pack_id)
    package = Package.objects.get(id = pack_id)
    return render(request,'detail.html',{"package":package})
