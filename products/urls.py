from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductFormView

urlpatterns = [
    path('', ProductListView.as_view(), name="all_products"),
    path('add_product/', ProductFormView.as_view(), name="add_product"),
]