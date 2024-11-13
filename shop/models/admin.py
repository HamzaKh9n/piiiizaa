from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Carts)
admin.site.register(CartItems)
admin.site.register(sellers)
admin.site.register(temp_order)
admin.site.register(Order)