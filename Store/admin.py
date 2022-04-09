from django.contrib import admin
from .models.products import Product
from .models.categories import Category
from .models.orders import Order
from .models.unit_type import Unit_Type
from .models.userprofile import UserProfile
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','quantity',  'unit', 'Unit_price','description', 'category','krishok','image_tag',]
    search_fields = ('name',)
    list_filter = ('category',)
    list_per_page = 50


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminUnit(admin.ModelAdmin):
    list_display = ['unit_name']


class AdminOrderDetails(admin.ModelAdmin):
    list_display = ['user','date', 'product', 'quantity','unit', 'price', 'email', 'phone', 'status']
    
    list_filter = ('product',)
    list_per_page = 50




admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Unit_Type, AdminUnit)
admin.site.register(UserProfile)
admin.site.register(Order, AdminOrderDetails)
