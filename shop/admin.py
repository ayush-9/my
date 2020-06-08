from django.contrib import admin

# Register your models here.
from .models import Types, Product, Contact, Orders, OrderUpdate
admin.site.register(Types)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)