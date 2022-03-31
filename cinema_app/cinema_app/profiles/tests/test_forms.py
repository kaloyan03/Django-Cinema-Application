import base64
from io import BytesIO

from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from cinema_app.profiles.forms import ProfileForm
from cinema_app.profiles.models import Profile

UserModel = get_user_model()

class ProfileFormTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        "email": "testtest@abv.bg",
        "password": '112313213qwe',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Kaloyan',
        'last_name': 'Tsvetkov',
        'age': 18,
        'profile_picture': SimpleUploadedFile(name='test_image.jpg',
                                              content=open(r"C:\Users\PC\Pictures\profile_photo-min.jpg", 'rb').read(),
                                              content_type='image/jpeg'),
    }

    def setUp(self) -> None:
        UserModel.objects.create(**self.VALID_USER_CREDENTIALS)

    def test__when_form_has_correct_data__expect_form_to_be_valid(self):
        form = ProfileForm(user=UserModel.objects.first(), data=self.VALID_PROFILE_DATA, files={"profile_picture": self.VALID_PROFILE_DATA['profile_picture']})

        self.assertTrue(form.is_valid())

    def test_create__profile_to_have_user__expect_correct_save_method(self):
        form = ProfileForm(user=UserModel.objects.first(), data=self.VALID_PROFILE_DATA,
                           files={"profile_picture": self.VALID_PROFILE_DATA['profile_picture']})

        if form.is_valid():
            form.save()
            profile = Profile.objects.first()

            self.assertTrue(profile.user)



