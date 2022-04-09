# from django import forms
# from django.contrib.auth.models import User, Group
# from django.contrib.auth.forms import UserCreationForm
# from .models.userprofile import UserProfile
# from django.forms import ModelForm

# class CustomerRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
   
#         #group = Group(name='Farmer')
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# class UserProfileForm(ModelForm):
#     class Meta:
#         model = UserProfile
   
#         #group = Group(name='Farmer')
#         fields = '__all__'