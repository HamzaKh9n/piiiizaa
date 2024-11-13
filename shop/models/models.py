import datetime
from django.db import models
import uuid
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class MainModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4  , editable=False , primary_key=True)
    class Meta:
        abstract = True

class sellers(models.Model):
    name = models.CharField(max_length=100 , default ='none')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    gmail = models.EmailField(max_length=250)
    phone = models.IntegerField()
    address =models.CharField(max_length=150 , default ='none')
    state = models.CharField(max_length=50 , default ='none')
    city = models.CharField(max_length=50 , default ='none')


class Pizza(MainModel):
    img = models.FileField(upload_to='images' , default=None)
    ex_img = models.FileField(upload_to='images' , default='images/image2.png')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    owner = models.ForeignKey(sellers , on_delete=models.CASCADE , default=0)
    descrip = models.CharField(max_length=100 , default='Pizza')

class Carts(MainModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE)   

class CartItems(MainModel):
    cart = models.ForeignKey(Carts , on_delete=models.CASCADE , related_name='cart_items')
    pizzas = models.ForeignKey(Pizza , on_delete=models.CASCADE  , related_name='cart_pizzas')
    quantity = models.IntegerField(default=1)

class temp_order(MainModel):
    order_id = models.UUIDField(default=uuid.uuid4 , editable=False ,null=False)
    pizza = models.ForeignKey(Pizza , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class Order(MainModel):
    order = models.ForeignKey(temp_order , on_delete=models.CASCADE)
    owner = models.ForeignKey(sellers , on_delete=models.CASCADE)
    time = models.TimeField(default=None)
    date = models.DateField(default=None)
