from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from cinema_app.profiles.models import Profile

UserModel = get_user_model()


class CompleteProfileViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'kalata8823@abv.bg',
        'password': '123123123213sada',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Kaloyan',
        'last_name': 'Tsvetkov',
        'profile_picture': SimpleUploadedFile(name='test_image.jpg',
                                              content=open(r"C:\Users\PC\Pictures\profile_photo-min.jpg", 'rb').read(),
                                              content_type='image/jpeg'),
        'age': 18,
    }

    def setUp(self) -> None:
        UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

    def test_get__correct_template_given__expect_correct_template(self):
        response = self.client.get(reverse('complete profile'))
        self.assertTemplateUsed(response, 'profile/complete_profile.html')

    def test_get__incorrect_template_given__expect_incorrect_template(self):
        response = self.client.get(reverse('list movies'))
        self.assertTemplateNotUsed(response, 'profile/complete_profile.html')

    def test_post__create_profile_expect_to_create_profile(self):
        response = self.client.post(reverse('complete profile'), data=self.VALID_PROFILE_DATA)
        profile = Profile.objects.first()

        # test if redirect works
        expected_url = reverse('profile')
        self.assertRedirects(response, expected_url)

        self.assertIsNotNone(profile)

        # test get_form_kwargs - expected profile to have user attribute
        self.assertIsNotNone(profile.user)


    # def test_post__check_kwargs_working_corectly__expect_profile_to_have_user(self):
    #     self.client.post(reverse('complete profile'), data=self.VALID_PROFILE_DATA)
    #     profile = Profile.objects.first()
    #
    #     self.assertIsNotNone(profile.user)



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

    }

    def setUp(self) -> None:
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)
        Profile.objects.create(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=self.VALID_PROFILE_DATA['last_name'],
            profile_picture=self.VALID_PROFILE_DATA['profile_picture'],
            age=self.VALID_PROFILE_DATA['age'],
            user=user
        )

    def test_get__correct_template_given__expect_correct_template(self):
        profile = Profile.objects.all()[0]
        response = self.client.get(reverse('delete profile', kwargs={'pk': profile.id}))
        self.assertTemplateUsed(response, 'profile/delete_profile.html')

    def test_post__delete_profile_and_user__expect_to_delete_profile_and_user(self):
        profile = Profile.objects.first()
        response = self.client.post(reverse('delete profile', kwargs={'pk': profile.pk}))

        # check redirect
        expected_url = reverse('sign in')
        self.assertRedirects(response, expected_url)

        profiles = Profile.objects.all()
        users = UserModel.objects.all()

        # check if profile and user are deleted
        self.assertEqual(len(profiles), 0)
        self.assertEqual(len(users), 0)


class ShowProfileViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'kalata8823@abv.bg',
        'password': '123123123213sada',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Kaloyan',
        'last_name': 'Tsvetkov',
        'profile_picture': SimpleUploadedFile(name='test_image.jpg',
                                              content=open(r"C:\Users\PC\Pictures\profile_photo-min.jpg", 'rb').read(),
                                              content_type='image/jpeg'),
        'age': 18,
    }

    def setUp(self) -> None:
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)
        Profile.objects.create(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=self.VALID_PROFILE_DATA['last_name'],
            profile_picture=self.VALID_PROFILE_DATA['profile_picture'],
            age=self.VALID_PROFILE_DATA['age'],
            user=user
                               )

    def test_get__correct_template_given__expect_correct_template(self):
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_get__incorrect_template_given__expect_incorrect_template(self):
        response = self.client.get(reverse('list movies'))
        self.assertTemplateNotUsed(response, 'profile/profile.html')

    def test_get__context__expect_context_to_have_profile(self):
        response = self.client.get(reverse('profile'))
        profile = response.context['profile']

        self.assertIsNotNone(profile)
