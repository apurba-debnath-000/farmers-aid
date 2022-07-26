from Store.models.products import Product
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db import models
from django.forms import fields
from .models.userprofile import UserProfile

class FarmerRegistrationForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']
       

class User_Form(UserChangeForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
######------Extra Information-------------->>>>>>>

class InfoUserProfileForm(forms.ModelForm):
    
    class Meta():
        model = UserProfile
        fields = ('address', 'national_id_no', 'phone', 'image', 'national_id')

        widgets = {

                'phone': forms.TextInput(attrs={'class':'form-control',"pattern":"[0][1][2-9][0-9]{8}", 'title':'follow this pattern: ex:-017-000-000-00'}),
                

            }

    # # def clean(self):
    #     cleaned_data = super(InfoUserProfileForm, self).clean()
        
    #     phone = self.cleaned_data.get('phone')
    #     if len(phone) < 11:
    #         raise forms.ValidationError("Phone no. should not be more than 11 char long")
    #     # elif not type(phone) == int:
    #     #     raise forms.ValidationError("Phone no. must be number")

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise forms.ValidationError("Phone no. should not be leass or more than 11 char long")
        return phone




class CustomerRegForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =  "__all__"
    
#Question??
    # def is_Exist_email(self):
    #     email = self.Cleaned_data.get("email")
    #     user_count = User.objects.filter(email=email).count()
    #     if user_count > 0:
    #         raise forms.ValidationError('Sorry! this email already exits ')
    #     return email

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control,custom-file-input'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_stuff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    # last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',  'last_login', 'is_superuser', 'is_stuff', 'is_active','date_joined')
