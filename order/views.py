from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForm
from .models import Order

def list_orders(request):
    return render(request,'order/list_orders.html')


def add_order(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'order/add_order.html',context)

def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'order/add_order.html', context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request,'order/delete_order.html',context)
