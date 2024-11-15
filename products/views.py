from django.shortcuts import render
from django.views.generic.base import TemplateView
# MODELS
from products.models import Product

class ProductListView(TemplateView):
    template_name = "products/products.html"
    
    def get_context_data(self):
        products_list = Product.objects.all()
        return {
            "products_list" : products_list
        }