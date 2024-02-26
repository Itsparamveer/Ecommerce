from django.conf import settings

from .models import Product

from django.core.exceptions import ObjectDoesNotExist
class  Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
               cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
     for p in list(self.cart.keys()):
        try:
            product = Product.objects.get(pk=p)
            self.cart[str(p)]['product'] = product
            item = self.cart[str(p)]
            item['total_price'] = int(item['product'].price * item['quantity']) / 100
            yield item
        except Product.DoesNotExist:
            self.cart.pop(str(p), None)  
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    


    def add(self, product_id,quantity=1, update_quantity= False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'id': product_id}
        
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
        
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID]=self.cart
        self.session.modified = True
        
    def remove(self,product_id):
        if (product_id) in self.cart:
            del self.cart[(product_id)]
            self.save()
            
    

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        
        return int(sum(item['product'].price * item['quantity'] for item in self.cart.values())) / 100