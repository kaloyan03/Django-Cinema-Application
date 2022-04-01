from django import test as django_test

from cinema_app.cinema_auth.forms import SignUpForm


class SignUpFormTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'testtest@abv.bg',
        'password1': '12312231213qwe',
        'password2': '12312231213qwe',
    }

    def test__when_form_has_correct_data__expect_form_to_be_valid(self):
        form = SignUpForm(data=self.VALID_USER_CREDENTIALS)

        self.assertTrue(form.is_valid())

    def test_create__profile_to_have_user__expect_correct_save_method(self):
        form = SignUpForm(data=self.VALID_USER_CREDENTIALS)

        if form.is_valid():
            user = form.save()

            self.assertIsNotNone(user)
