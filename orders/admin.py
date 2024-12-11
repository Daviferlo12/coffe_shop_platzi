from django.contrib import admin
from .models import Order, Order_product

class OrderProductInLineAdmin(admin.TabularInline):
    model = Order_product
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInLineAdmin
    ]

    
admin.site.register(Order, OrderAdmin)
    

