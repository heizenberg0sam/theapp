from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import OrderForm , LawyerForm , UserForm
from . models import OrderNow, lawyer
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,'base/home.html')



def ordernow(request):
    lawyers = lawyer.objects.all()
    order = OrderForm()
    if request.method == 'POST':
       
        form = OrderForm(request.POST)
        
        
        if form.is_valid():
          userfreeze = form.save() #########nice!!!!!!!!!!!!!!!!!!!!
          userfreeze.user = request.user
          userfreeze.save()
          return (redirect('done'))
    
    contex = {"form":order , "lawyers":lawyers}
    return render(request, 'base/ordernow.html',contex)

def addLawyer(request):
    add=LawyerForm()
    if request.method == "POST":
        form = LawyerForm(request.POST)
        if form.is_valid():
            form.save()
    contex = {"form":add}

    return render(request , 'base/addlawyer.html',contex)
     

def orders(request):
    orders= OrderNow.objects.all()
    contex = {"orders":orders}
    return render(request, 'base/orders.html',contex)

def loginPage(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
           user = User.objects.get(username= username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request , username=username , password= password)
        if user is not None:
            login(request , user)
            return redirect('smsverify')
        else:
            messages.error(request, 'Password is incorrect')


    return render(request , 'base/login_register.html',{"page":page}) 

def userregister(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
           user =  form.save(commit=False)
           user.save()
           login(request,user)
           return redirect('editprofile')
        else:
               messages.error(request, 'shiteeeeeeeeeee')


    contex={'form':form}

    return render(request , 'base/login_register.html',contex)
     
@login_required(login_url='login')
def order(request , pn):

    
    orders= OrderNow.objects.filter(chosenlawyer__data__contains=pn).order_by('created')
    if pn == 'ashkan':
        orders= OrderNow.objects.all().order_by('created')

    context={'orders':orders}
    return render(request,'base/order.html',context)

def userOrders(request):
    orders= OrderNow.objects.filter(user = request.user)
    context={"orders":orders}
    return render(request,'base/userorders.html',context)






def smsverify(request):

    if request.method=="POST":
        return redirect('home')
    return render(request,'base/sms-verify.html')
 




def logoutPage(request):
    logout(request)
    return redirect('home')

def done(request):
    return render(request , 'base/done.html')


def editprofile(request):
    
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid:
            form.save()
            return redirect('smsverify')
        else:
               messages.error(request, 'shiteeeeeeeeeee')    
    return render(request, 'base/profileupdate.html',{'form':form})


def lawyersPage(request):
    lawyers = lawyer.objects.all()
    context = {'lawyers':lawyers}
    return render(request,'base/lawyers.html',context)

def lawyerProfile(request,pk)    :
    thelawyer = lawyer.objects.get(id=pk)
    context={"lawyer":thelawyer}
    return render(request,'base/lawyerprofile.html',context)



def social(request)    :
    return render(request , 'base/social.html')