from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from cinema_app.profiles.models import Profile

UserModel = get_user_model()


class ProfileModelTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        "email": "testtest@abv.bg",
        "password": '112313213qwe',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Kaloyan',
        'last_name': 'Tsvetkov',
        'profile_picture': SimpleUploadedFile(name='test_image.jpg',
                                              content=open(r"C:\Users\PC\Pictures\profile_photo-min.jpg", 'rb').read(),
                                              content_type='image/jpeg'),
        'age': 18,
        'user': UserModel.objects.first(),
    }

    def setUp(self) -> None:
        UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)

    def test_post__when_first_name_starts_with_capital_letter__expect_success(self):
        user = UserModel.objects.first()
        profile = Profile.objects.create(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=self.VALID_PROFILE_DATA['last_name'],
            profile_picture=self.VALID_PROFILE_DATA['profile_picture'],
            age=self.VALID_PROFILE_DATA['age'],
            user=user
        )
        self.assertIsNotNone(profile)

    def test_post__when_last_name_starts_with_capital_letter__expect_success(self):
        user = UserModel.objects.first()
        profile = Profile.objects.create(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=self.VALID_PROFILE_DATA['last_name'],
            profile_picture=self.VALID_PROFILE_DATA['profile_picture'],
            age=self.VALID_PROFILE_DATA['age'],
            user=user
        )
        self.assertIsNotNone(profile)

    def test_post__when_first_name_is_not_starting_with_capital_letter__expect_fail(self):
        user = UserModel.objects.first()
        profile = Profile.objects.create(first_name='kaloyan',
                                         last_name='Tsvetkov',
                                         profile_picture=SimpleUploadedFile(name='test_image.jpg',
                                                                            content=open(
                                                                                r"C:\Users\PC\Pictures\profile_photo-min.jpg",
                                                                                'rb').read(),
                                                                            content_type='image/jpeg'),
                                         age=18,
                                         user=user,
                                         )

        with self.assertRaises(ValidationError) as error_message:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(error_message)

    def test_post__when_last_name_is_not_starting_with_capital_letter__expect_fail(self):
        profile = Profile.objects.create(first_name='Kaloyan',
                                         last_name='tsvetkov',
                                         profile_picture=SimpleUploadedFile(name='test_image.jpg',
                                                                            content=open(
                                                                                r"C:\Users\PC\Pictures\profile_photo-min.jpg",
                                                                                'rb').read(),
                                                                            content_type='image/jpeg'),
                                         age=18,
                                         user=UserModel.objects.first(), )

        with self.assertRaises(ValidationError) as error_message:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(error_message)
