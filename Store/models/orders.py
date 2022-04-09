from Store.models.unit_type import Unit_Type
from Store.models.products import Product
from django.db import models
from .products import Product
from django.contrib.auth.models import User
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=300, blank=True, default='')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    unit = models.ForeignKey(Unit_Type, on_delete=models.CASCADE, default='kg')
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def __str__(self):
        return self.product.name

    @staticmethod
    def get_orders_by_user(user_id):
        return Order\
        .objects\
        .filter(user = user_id).order_by('-date')