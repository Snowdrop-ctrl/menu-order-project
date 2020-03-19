from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import Argon2PasswordHasher
from django.views.generic.edit   import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View,TemplateView,ListView,DetailView
from .forms import Menu_Form,order_Form,register_form,UserCreateForm
from menu_order_app.models import Menu,Order,Order_Item
from  . import models
#
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

######## Menu-Index #########

class index(TemplateView):
    template_name = 'index.html'

######## End-Menu-Index ########

def SingUp(request):
    register = False
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            register = True
    else:
        form = UserCreateForm()
    return render(request, "menu_order_app/signup.html",{'form':form,'register':register})
    

######### Menu-view ##########

@login_required
def add_dish(request):
    filled = False
    if request.method == 'POST':
        menu_form = Menu_Form(request.POST,request.FILES)
        if menu_form.is_valid():
            menu_form.save()
            filled = True
        else:
            print('not valid')
            return HttpResponse("not valid")
    else:
        menu_form = Menu_Form()
    return render(request,'menu.html',{'menu_form':menu_form,'filled':filled})

########## End Menu-view ##########
#
# ########## order-view ##########
#
def order_register_view(request):
    register = False

    if request.method == 'POST':
        order = order_Form(request.POST)
        if order.is_valid():
            order.save()
            
            register = True
        else:
            return HttpResponse(data.errors)
    else:
        order = order_Form()

    return render(request,'registration.html',{'order':order,'register':register})



# class menu_dish(ListView):
#      model = models.Menu

@login_required
def menu_dish(request):

    if request.method == 'POST':
        pass
        # menu = request.session.get('menu_id')
        # print(menu)
        
    else:
        item = Menu.objects.order_by('id')
    return render(request,'menu_dish.html',{'item':item})

########## End order-view ##########








########## order-Item ##########


# def order_item_view(request):

#     menu = Menu_Form()
#     order = order_Form()

#     item = order_item_form(menu,order)
#     item.save()

#     # if request.method == 'POST':
        
#     #     print(request.POST['order_items'])
#     #     menu = request.POST.get()
#     #     # print(menu)
#     #     return HttpResponse(menu)

#     return HttpResponse("Thanks")


########## End order-Item ##########











# def regiteration_form(request):
#     registered = False
#
#
#     if request.method == 'POST':
#         user_form = User_Register_Form(data=request.POST)
#         member_form = Members_Register_Form(data=request.POST)
#
#         if member_form.is_valid() and user_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             member = member_form.save(commit=False)
#             member.user = user
#             member.save()
#             registered = True
#
#         else:
#             print(user_form.errors,member_form.errors)
#
#     else:
#         member_form = Members_Register_Form()
#         user_form = User_Register_Form()
#
#     return render(request,'Menu_Order_Html/Registration.html',{'member_form':member_form,'user_form':user_form,'registered':registered})

