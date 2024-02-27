from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout as logoutUser
from django.contrib.auth import authenticate,login as loginUser ,logout
from apps.store.models import Product,Category
from apps.vender.forms import productForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages
# from captcha.fields import ReCaptchaField
import json



# Create your views here.

def login(request):
    return render(request,"login.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('product')

    if request.method == 'GET':
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST )
        # captcha = ReCaptchaField()
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None: 
                request.session['username'] = user.username  
                request.session['password'] = user.password     
                loginUser(request,user)
            return redirect("product")
            print("Authenticated",user)
        else:
            context = {"form":form}
            return render(request, 'login.html',context=context)

def signup(request):
    return render (request,'signup.html')

def signup(request):
    if request.method == 'GET':
        form=UserCreationForm()
        context={"form":form}
        return render(request,'signup.html',context=context)
    else:
        print(request.POST)
        form=UserCreationForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)
        
@login_required(login_url='login')
def product(request):
    if request.user.is_authenticated:
        user = request.user
        products = Product.objects.filter(user=user)
        p=Paginator(products,9)
        # print(products,p.num_pages)
        page_number=request.GET.get('page',1)
        page=p.page(page_number)
        # print( request.session.get('username'))
        # print(request.session.get('password'))
        context={'products':page}
        return render (request,'product.html',context)

def addproduct(request):
     if request.user.is_authenticated:
        form =  productForm()
        product=Product.objects.all
        return render(request,'addproduct.html',context={'form':form,'product':product})
    
    
    
def add_item(request):
        user = request.user
        form =productForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            product = form.save(commit=False)
            product.user=user
            product.save()
            messages.success(request, 'Product created successfully!')
            return redirect("product")
        else:
            form = productForm()
            return render(request, 'index.html', context={'form': form})
    
    
    
def editproduct(request,slug,id):
    product = get_object_or_404(Product, pk=id)
    products = Product.objects.filter(slug=slug)
    if request.method == 'POST':
        if 'delete' in request.POST:  
            product.delete()
            messages.success(request, 'Product delete successfully!')
            return redirect('product')
        else:
            form = productForm(request.POST, request.FILES, instance=product) 
            if form.is_valid():
                form.save()
                messages.success(request, 'Product update successfully!')
                return redirect('product')
            
    else:
        form = productForm(instance=product)
    return render(request, 'editproduct.html', {'form': form, 'products': products})
    
def searchproduct(request):
    if request.method == 'GET':
        name = request.GET.get('searchproduct')
        form =productForm()
        products = Product.objects.filter(title__icontains=name)
        return render(request,'index.html',context={'form':form,'products':products})
    
def venderproduct(request):
     if request.user.is_authenticated:
        user = request.user
        if request.method == 'GET':
            name = request.GET.get('venderproduct')
            form =productForm()
            products = Product.objects.filter(title__icontains=name,user=user)
            return render(request,'product.html',context={'form':form,'products':products})
        
def logout(request):
    logoutUser(request)
    return redirect('index')