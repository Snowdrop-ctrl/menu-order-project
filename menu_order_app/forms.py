from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,User
from django.contrib.auth import get_user_model
from .models import Menu,Order,Order_Item,register
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

from django.core import validators


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        

    def __init__(self,*args,**Kwargs):
        super().__init__(*args,**Kwargs)
        self.fields['username'].label = 'Your Name'

        
# ########## Menu-form ##########

class Menu_Form(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

########## End Menu-form ##########
class register_form(forms.ModelForm):
	class Meta:
		model = register
		fields = ['full_name']


class order_Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    # def clean(self):
    #  	super(order_Form, self).clean()

    #  	name = self.cleaned_data.get('name')
    #  	mobile_no = self.cleaned_data.get('mobile_no')

    #  	if len(name) < 4:
    #  		self._errors['name'] = self.error_class([
    #  			'minimum 4 character required'])
    #  	if mobile_no:
    #  		self._errors['mobile_no'] = self.error_class([
    #  			'Enter valid mobile number.'])


class order_item_form(forms.ModelForm):
	class Meta:
		model = Order_Item
		fields = '__all__'



















############# START member registrations and validatins #############

# class restaurant_name(forms.Form):
#     pass

# class Member_Form(forms.Form):
#     Restaurant_name = restaurant_name()
#     owner_name = forms.CharField()
#     manager_name = forms.CharField()
#     add = forms.CharField()
#     mobile_no = PhoneNumberField()
#
#     def __init__(self):
#         pass

# class Members_Register_Form(forms.ModelForm):
#     class Meta():
#         model = Member
#         fields = ('Restaurant_name','owner_name','manager_name','add','mobile_no')

############# END member registrations and validatins #############


############# START user registrations and validatins #############

# class User_Register_Form(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model = User
#         fields = ('username','password','email')


############# END user registrations and validatins #############

############# START login  #############

class Login_form(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()

############# END login #############

############# START Enquery Form #############

# class Enquery_Form(forms.ModelForm):
#     class Meta():
#         pass

############# START Enquery Form #############

