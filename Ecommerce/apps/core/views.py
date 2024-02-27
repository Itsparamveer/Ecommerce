from django.shortcuts import render 

from apps.store.models import Product

 # Create your views here.
def index(request):
<<<<<<< HEAD
    products =Product.objects.all()[0:5]
    return render(request,'index.html',{
        'products':products})

def about(request):
    return render(request , 'about.html')

=======
     products =Product.objects.all()[0:5]
     return render(request,'index.html' ,{
         'products':products})

def about(request):
     return render(request , 'about.html')
>>>>>>> 57f03f1218b00303d4ec8310f88c18fe0d941ef3
