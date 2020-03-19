from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User,PermissionsMixin
from django.contrib import auth
from django.core.validators import validate_slug, validate_email
from django.core import validators





# class Member(models.Model):
#     # HEAR_OPTION = (
#     #     ('google','google'),
#     #     ('some people','some people'),
#     #     ('youtube','youtube')
#     # )
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     Restaurant_name = models.CharField(max_length=100, blank=False)
#     owner_name = models.CharField(max_length=100, blank=False)
#     manager_name = models.CharField(max_length=100, blank=False)
#     add = models.CharField(max_length=200,blank=False)
#     mobile_no = PhoneNumberField(null=False, blank=False, unique=True)
#     # where_do_you_hear_about_us = models.CharField(max_length=40,choices=HEAR_OPTION)
#     membership_plan = models.CharField(max_length=20)
#     date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         pass

class register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    def __str__(self):
        return self.full_name

class Menu(models.Model):
    # member = models.ForeignKey(Member,on_delete=models.CASCADE)
    categories = models.CharField(max_length=50, blank=False)
    photo = models.ImageField(upload_to='media/',blank=True)
    dish_name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.dish_name

class Order(models.Model):
    name = models.CharField(max_length=20)
    mobile_no = PhoneNumberField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Order_Item(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    

