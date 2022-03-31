from django import test as django_test
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CinemaUserTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        "email": "testtest@abv.bg",
        "password": '112313213qwe',
    }


    def test_post__when_data_is_valid__expect_to_create_user(self):
        UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)

        user = UserModel.objects.first()

        self.assertIsNotNone(user)

    def test_post__when_data_is_valid_user_is_staff__expect_user_to_be_staff(self):
        UserModel.objects.create_user(
            email=self.VALID_USER_CREDENTIALS['email'],
            password=self.VALID_USER_CREDENTIALS['password'],
            is_staff=True,
        )

        user = UserModel.objects.first()

        self.assertTrue(user.is_staff)
