from django.forms import Form, ModelForm
from .models import Order_product


class Order_productForm(ModelForm):
    class Meta:
        model = Order_product
        fields = ["product"]
