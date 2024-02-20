from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('product/',views.product,name='product'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('add_item/',views.add_item,name='add_item'),
    path('<slug:slug>/<int:id>',views.editproduct,name='editproduct'),
    

]  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
