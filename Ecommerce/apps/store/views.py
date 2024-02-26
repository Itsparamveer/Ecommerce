from django.shortcuts import redirect, get_object_or_404,render
from django.db.models import Q
from .cart import Cart
from .models import Category, Product

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')

def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)
    
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')
def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {
        'query': query,
        'products': products,
    })

def category_detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        products = category.products.all()  # Assuming you want all products in the category
    except Category.DoesNotExist:
        # Handle case where category does not exist
        category = None
        products = []

    return render(request, 'category_detail.html', {
        'category': category,
        'products': products
    })

def product_detail(request,category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product_detail.html', {
        'product': product
    })


def cart_view(request):
    cart = Cart(request)
    
    return render(request, 'cart_view.html', {'cart': cart
        })
