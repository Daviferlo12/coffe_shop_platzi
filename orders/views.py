from django.shortcuts import render
from django.views.generic import DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Order, Order_product
from .forms import Order_productForm


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()


class CreateOrderProduct(LoginRequiredMixin, CreateView):
    model = Order_product
    # template_name = "orders/create_order.html"
    form_class = Order_productForm
    success_url = reverse_lazy("MyOrder")

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(is_active=True, user=self.request.user)

        form.instance.order = order
        form.instance.quantity = 1
        form.save()

        return super().form_valid(form)


class DeleteOrderProduct(LoginRequiredMixin, DeleteView):
    model = Order_product
    success_url = reverse_lazy("MyOrder")
    # template_name = 'orders/confirm_delete_product.html'

    def get_object(self, queryset=None):
        """
        Obtiene el producto a eliminar asegurando que pertenece al usuario autenticado.
        """
        return get_object_or_404(
            Order_product, pk=self.kwargs["pk"], order__user=self.request.user
        )
