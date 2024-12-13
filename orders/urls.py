from django.urls import path
from .views import MyOrderView, CreateOrderProduct, DeleteOrderProduct


urlpatterns = [
    path("my_order/", MyOrderView.as_view(), name= "MyOrder"),
    path("add_product_order/", CreateOrderProduct.as_view(), name="CreateOrderProduct"),
    path("delete_product_order/<int:pk>/", DeleteOrderProduct.as_view(), name="DeleteOrderProduct")
]