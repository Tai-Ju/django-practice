from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def hello(request):
    return HttpResponse("Hello,World!")
def home(request):
    context = {
        "title": "歡迎頁面",
        "subtitle": "歡迎來到我們的網站",
        "image": "cat.jpg",
        "products": [
            {
                "name": "Product 1",
                "price": 100,
                "image": "product1.webp",
            },
            {
                "name": "Product 2",
                "price": 200,
                "image": "product2.webp",
            },
            {
                "name": "Product 3",
                "price": 300,
                "image": "product3.jpg",
            },
        ],    

    }

    return render(request, "home.html", context)

def home2(request):
    
    person = {
            "name": "John",
            "age": 20,
    }
    person2 = {
            "name": "Mary",
            "age": 21,
    }
    person3 = {
            "name": "Bob",
            "age": 22,
    }
    context = {
        "persons": [person, person2, person3],
        "version": 1.0,
        "date": datetime.now(),
        "last_update": datetime.now(),
    }
    return render(request, "home2.html", context)
    
def member(request):
    return render(request, "member.html")

def product(request):
    # products = Product.objects.all()
    products = Product.objects.get(id=3)

    context = {
        "products": products,
    }
    return render(request, "product.html", context)