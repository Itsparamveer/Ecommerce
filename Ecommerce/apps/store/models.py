from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

from io import BytesIO
from PIL import Image



# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        
        verbose_name_plural="Categories"

    def __str__(self):
            return self.title
    
class Product(models.Model):
     DARFT="draft"
     WAITING_APPROVAL="waitingapproval"
     ACTIVE="active"
     DELETED="delected"

     STATUS_CHOICES=(
     (DARFT,"Draft"),
     (WAITING_APPROVAL,"Waitingapproval"),
     (ACTIVE,"Active"),
     (DELETED,"Delected"),
     )

     user= models.ForeignKey(User,related_name='products', on_delete=models.CASCADE)
     category=models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)

     title = models.CharField(max_length=50)
     slug = models.SlugField(max_length=50)
     description = models.TextField(blank=True)
     price=models.IntegerField()
     image = models.ImageField(upload_to='uploads/product_images/', blank=True ,null=True)
     thumbnail = models.ImageField(upload_to='uploads/product_images/thumbnail', blank=True, null=True)
     created_at=models.DateField(auto_now_add=True)
     updated_at=models.DateField(auto_now=True)
<<<<<<< HEAD
     images = models.ImageField(upload_to="images/",blank=True,null=True)

=======
     status=models.CharField(max_length=50, choices=STATUS_CHOICES , default=ACTIVE)
>>>>>>> 57f03f1218b00303d4ec8310f88c18fe0d941ef3
     class Meta:
           ordering=('-created_at',)
     
     def __str__(self):
            return self.title
     
     def get_display_price(self):
           return self.price/100
<<<<<<< HEAD
       
     
=======
   
     def get_thumbnail(self):
      if self.thumbnail:
        return self.thumbnail.url
      elif self.image:
        self.thumbnail = self.make_thumbnail(self.image)
        self.save()
        return self.thumbnail.url
      else:
        return 'https://via.placeholder.com/240x240x.jpg'

     def make_thumbnail(self, image, size=(300, 300), quality=85):
      try:
        with Image.open(image) as img:
            img.thumbnail(size)
            thumb_io = BytesIO()
            img.convert('RGB').save(thumb_io, format='JPEG', quality=quality)
            name = image.name.replace('uploads/product_images/', '')
            thumbnail = File(thumb_io, name=name)
            return thumbnail
      except Exception as e:
        print("Error creating thumbnail:", e)
        return None  # Return None if thumbnail creation fails


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    
    def get_display_price(self):
        return self.price / 100
>>>>>>> 57f03f1218b00303d4ec8310f88c18fe0d941ef3
