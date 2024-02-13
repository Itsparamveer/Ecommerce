from django.shortcuts import render ,get_object_or_404

# Create your views here.
from .models import Product ,Category

def category_detail(request , slug):
    category = get_object_or_404(Category ,slug=slug)
    products = category.products.all()
    return render(request , 'category_detail.html',{
        'category':category,
        'products':products
        })

def product_detail(request,category_slug , slug):
    product=get_object_or_404(Product,slug=slug)

    return render (request , 'product_detail.html', {
        'product':product
        })