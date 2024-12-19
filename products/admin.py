from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "available"]
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)
