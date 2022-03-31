from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from star_ratings.models import Rating

from cinema_app.movies.models import Movie, Ticket

UserModel = get_user_model()


class ShowLandingPageViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        "email": "testtest@abv.bg",
        "password": "12321323123qwe",
        "is_staff": True,
    }

    VALID_MOVIE_DATA = {
        'title': 'Avatar',
        'image': SimpleUploadedFile(name='test_image.jpg',
                                    content=open(r"C:\Users\PC\Pictures\Softuni Cinema Project Photos\spider-man.jpg",
                                                 'rb').read(), content_type='image/jpeg'),
        'trailer_video': 'https://www.youtube.com/watch?v=zAH-GjT4Jpw',
        'genre': 'Adventure',
        'year': 2010,
        'description': 'Ben-10 The Movie.',
        'duration': 140,
        'category': 'B',
    }

    def setUp(self) -> None:
        Movie.objects.create(**self.VALID_MOVIE_DATA)
        Ticket.objects.create(price=15, movie=Movie.objects.first())
        Rating.objects.create(average=5.0, count=1, total=5, object_id=Movie.objects.first().id, content_type_id=7)

    def test_get__when_correct_template_given__expect_success(self):
        response = self.client.get(reverse('landing page'))

        self.assertTemplateUsed(response, 'landing_page.html')

    def test_get__when_two_movies_rated__expect_movies_in_context(self):
        movie2 = Movie.objects.create(
            title='Avatar2',
            image=SimpleUploadedFile(name='test_image.jpg',
                                     content=open(r"C:\Users\PC\Pictures\Softuni Cinema Project Photos\spider-man.jpg",
                                                  'rb').read(), content_type='image/jpeg'),
            trailer_video='https://www.youtube.com/watch?v=zAH-GjT4Jpw',
            genre='Adventure',
            year=2010,
            description='Ben-10 The Movie.',
            duration=140,
            category='B',
        )
        Ticket.objects.create(price=15, movie=Movie.objects.get(id=movie2.id))
        Rating.objects.create(average=5.0, count=1, total=5, object_id=movie2.id, content_type_id=7)

        response = self.client.get(reverse('landing page'))

        movies = response.context['movies']

        self.assertEqual(len(movies), 2)

    def test_get__when_user_is_staff__expect_is_staff_to_be_true(self):
        UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse('landing page'))

        is_staff = response.context['user_is_staff']

        self.assertTrue(is_staff)
