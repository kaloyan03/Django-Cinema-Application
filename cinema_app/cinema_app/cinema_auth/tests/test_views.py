from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()

class SignUpViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'testtest@abv.bg',
        'password1': '12312231213qwe',
        'password2': '12312231213qwe',
    }

    def test_get__correct_template__expect_correct_template(self):
        response = self.client.get(reverse('sign up'))

        self.assertTemplateUsed(response, 'auth/sign_up.html')

    def test_get__context__expect_form_in_context(self):
        response = self.client.get(reverse('sign up'))

        form = response.context['form']

        self.assertIsNotNone(form)

    def test_post__create_user__expect_to_create_user_and_login(self):
        response = self.client.post(reverse('sign up'), data=self.VALID_USER_CREDENTIALS)

        # check correct url to redirect
        expected_url = reverse('list movies')
        self.assertRedirects(response, expected_url)

        user = UserModel.objects.first()

        self.assertIsNotNone(user)
