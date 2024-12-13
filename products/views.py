from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response

# MODELS
from products.models import Product
from products.forms import ProductForm
from .serializers import ProductSerializer

class ProductListView(TemplateView):
    template_name = "products/products.html"
    
    def get_context_data(self):
        products_list = Product.objects.all()
        return {
            "products_list" : products_list
        }
        
class ProductFormView(LoginRequiredMixin, FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("all_products")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
    