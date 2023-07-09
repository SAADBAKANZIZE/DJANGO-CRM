from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from order.filtres import OrderFilter
def list_customers(request,pk):
    customer=Customer.objects.get(id=pk)
    order=customer.order_set.all()
    total_order=order.count()
    myFilter=OrderFilter(request.GET,queryset=order)
    order=myFilter.qs
    context={'customer':customer,'order':order,'total_order':total_order,'myFilter':myFilter}
    return render(request, 'customer/list_customers.html',context)

