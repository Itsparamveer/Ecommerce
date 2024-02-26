from django.shortcuts import render 

from apps.store.models import Product

 # Create your views here.
def index(request):
     products =Product.objects.all()[0:5]
     return render(request,'index.html' ,{
         'products':products})

def about(request):
     return render(request , 'about.html')