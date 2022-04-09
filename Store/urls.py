
from django import urls
from django.contrib import admin
from django.urls import path
from . import views

from .views import *
from .views import Cart, Checkout, OrderView, ViewFarmer
from .middlewares.auth import auth_middleware
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('', views.index, name='home'),
    path('customer_reg', views.customer_reg, name="cus_reg"),
    path('farmer_registration', views.farmer_reg, name = 'fa_reg'),
    path('officer_registration', views.agri_officer_reg, name = 'agri_officer_reg'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', auth_middleware(views.profile_view), name='profile'),
    path('edit_profile/',views.edit_profile, name='edit_profile_info'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('viewPro/<int:pk>', ViewProduct.as_view(), name='productDetails'),
    path('viewFar/<int:pk>', ViewFarmer.as_view(), name='farmerDetails'),

    path('check-out',auth_middleware(Checkout.as_view()), name='checkout'),
    
    path('return_login/', views.return_login, name='return_login'),
    path('typeSign', views.typesSign, name='type_Sign'),
    path('order/', auth_middleware(OrderView.as_view()), name='order_page'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name= 'profile/changePass.html') )
    path('password/', PasswordsChangeView.as_view(template_name= 'profile/changePass.html') ),
    path('password_success/', views.password_success, name="password_success"),
    #path('edit_profile/', UserEditView.as_view(), name= "edit_profiles"),
    
    #path('farmer_reg/', views.farmer_reg)
]
