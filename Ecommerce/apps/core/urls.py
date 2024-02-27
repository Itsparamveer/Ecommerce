from django.urls import path
from django.contrib import admin
from  .views import index, about
from .import views
from apps.store import cart
urlpatterns = [
    path('',index,  name='index'),
    path('',about ,name='about'),
     path('cart/', views.cart_view, name='cart_view'),
    path('admin/',admin.site.urls),
    ]
