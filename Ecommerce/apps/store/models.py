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
     status=models.CharField(max_length=50, choices=STATUS_CHOICES , default=ACTIVE)
     class Meta:
           ordering=('-created_at',)
     
     def __str__(self):
            return self.title
     
     def get_display_price(self):
           return self.price/100
   
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
