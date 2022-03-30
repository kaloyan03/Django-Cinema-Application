from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

UserModel = get_user_model()


class CompleteProfileViewTests(django_test.TestCase):
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
        UserModel.objects.create(**self.VALID_USER_CREDENTIALS)

    def test_get__correct_template_given__expect_correct_template(self):
        pass

    def test_get__incorrect_template_given__expect_incorrect_template(self):
        pass

    def test_post__when_success__expect_correct_redirect(self):
        pass

    def test_post__get_kwargs__expect_to_add_user_to_kwargs(self):
        pass

    def test_post__form_valid__expect_to_have_user_in_kwargs(self):
        pass


class DeleteProfileViewTests(django_test.TestCase):
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
        UserModel.objects.create(**self.VALID_USER_CREDENTIALS)

    def test_get__correct_template_given__expect_correct_template(self):
        pass

    def test_get__incorrect_template_given__expect_incorrect_template(self):
        pass

    def test_post__delete_profile_and_user__expect_to_delete_profile_and_user(self):
        pass

    def test_post__when_success__expect_correct_redirect(self):
        pass


class ShowProfileViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        "email": "testtest@abv.bg",
        "password": '112313213qwe',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Kaloyan',
        'last_name': 'Tsvetkov',
        'profile_picture': SimpleUploadedFile(name='test_image.jpg',
                                              content=open(r"C:\Users\PC\Pictures\profile_photo-min.jpg",
                                                           'rb').read(),
                                              content_type='image/jpeg'),
        'age': 18,
        'user': UserModel.objects.first(),
    }

    def setUp(self) -> None:
        UserModel.objects.create(**self.VALID_USER_CREDENTIALS)

    def test_get__correct_template_given__expect_correct_template(self):
        pass

    def test_get__incorrect_template_given__expect_incorrect_template(self):
        pass

    def test_get__context__expect_context_to_have_profile(self):
        pass
