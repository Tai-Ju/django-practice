from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

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
    

def product(request):
    if request.method == "GET":
        q = request.GET.get("q")
        if q:
            products = Product.objects.filter(name__icontains=q)
        else:
            products = Product.objects.all()
    else:
        products = Product.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        Product.objects.create(name=name, price=price, description=description)
        return redirect("ecommerce:product")
   
    context = {
        "products": products,
    }
    return render(request, "product.html", context)

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect("ecommerce:product")    

def edit_product(request, product_id):
    if request.method == "POST":
        product = Product.objects.get(id=product_id)
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.save()
        return redirect("ecommerce:product")    
    else:
        product = Product.objects.get(id=product_id)
        context = {
            "product": product,
        }
        return render(request, "edit_product.html", context)

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        product.name = request.POST.get("name", product.name) or product.name
        product.price = request.POST.get("price") or product.price
        product.description = request.POST.get("description", "")
        product.save()
        return redirect("ecommerce:product")
    return render(request, "edit_product.html", {"product": product})  