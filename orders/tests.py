from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class MyOrderViewTest(TestCase):

    def test_no_logged_user_should_be_redirected(self):
        url = reverse("MyOrder")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/users/login/?next=/orders/my_order/")

    def test_logged_user_should_be_redirected(self):
        url = reverse("MyOrder")
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
