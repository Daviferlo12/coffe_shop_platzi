from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductListViewTest(TestCase):

    def test_should_return_200(self):
        url = reverse("all_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products_list"].count(), 0)

    def test_should_return_200_when_add_product(self):
        url = reverse("all_products")
        Product.objects.create(name="test", description="test", price=5, available=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products_list"].count(), 1)
