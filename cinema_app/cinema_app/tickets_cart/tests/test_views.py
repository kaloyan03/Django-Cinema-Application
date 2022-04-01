from cart.cart import Cart
from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()

class CartViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'testtest@abv.bg',
        'password': '123313123231qwe',
    }

    def setUp(self) -> None:
        UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

    def test_get__correct_template_given__expect_correct_template(self):
        response = self.client.get(reverse('list movies'))

        self.assertTemplateUsed(response, 'checkout_cart.html')
