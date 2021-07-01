from django.shortcuts import render
from django.http import HttpResponse
from math import ceil

from .models import Product


def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        n_slides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, n), n_slides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("contact")


def tracker(request):
    return HttpResponse("tracker")


def search(request):
    return HttpResponse("search")


def product(request):
    return HttpResponse("product")


def checkout(request):
    return HttpResponse("checkhout")
