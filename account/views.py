from django.shortcuts import render
from .forms import CreateUser
# Create your views here.
def registerPage(request):
    form=CreateUser(request.POST)
    context={'form':form}
    return render(request,'account/register.html',context)

def loginPage(request):
    context={}
    return render(request,'account/login.html',context)