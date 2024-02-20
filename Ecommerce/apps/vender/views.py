from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser 
from apps.store.models import Product,Category
from apps.vender.forms import productForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def login(request):
    return render(request,"login.html")


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
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
        print(products)
        context={'products':products}
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
            return redirect('product')
        else:
            form = productForm(request.POST, request.FILES, instance=product) 
            if form.is_valid():
                form.save()
                return redirect('product')
    else:
        form = productForm(instance=product)
    return render(request, 'editproduct.html', {'form': form, 'products': products})
    
