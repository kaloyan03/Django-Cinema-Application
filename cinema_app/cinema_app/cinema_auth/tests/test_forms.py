from django import test as django_test

class SignUpFormTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'testtest@abv.bg',
        'password': '12312231213qwe',
    }

    def test__when_form_has_correct_data__expect_form_to_be_valid(self):
        pass

    def test_create__profile_to_have_user__expect_correct_save_method(self):
        pass