 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('product.urls'),),
    path('customer', include('customer.urls')),
    path('orders', include('order.urls')),

]
