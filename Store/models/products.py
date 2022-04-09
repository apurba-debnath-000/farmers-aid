from Store.models.userprofile import UserProfile
from django.db import models
from .categories import Category
from .unit_type import Unit_Type
from django.contrib.auth.models import User
from django.utils.html import format_html

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  default=1)
    unit= models.ForeignKey(Unit_Type, on_delete=models.CASCADE,  default='kg')
    Unit_price = models.IntegerField(default=0)

    #k_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to = 'upload/productsImg/')
    krishok = models.ForeignKey(User, limit_choices_to= { 'groups__name': 'Farmer'}, on_delete=models.CASCADE, default=1)

    def image_tag(self):
        return format_html(
            '<img src="/abcd/show/{}" style=" width:40px; height:40px; border-radius:50% "/>'.format(self.image)
        )
   
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    #Filtering by Category Id: 
    # this method will bring all products by its categoryID
    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    
    @staticmethod
    def get_product_by_ids(ids):
        return Product.objects.filter(id__in= ids)

    
