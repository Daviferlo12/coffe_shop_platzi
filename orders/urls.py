from django.urls import path
from .views import MyOrderView


urlpatterns = [
    path("my_order/", MyOrderView.as_view(), name= "MyOrder")
]