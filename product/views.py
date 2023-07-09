from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order
from customer.models import Customer
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    context={'orders':orders, 'customers':customers}

    return render(request,'product/accueil.html',context)
