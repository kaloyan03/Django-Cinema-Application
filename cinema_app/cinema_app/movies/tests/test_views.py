from django import test as django_test
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from cinema_app.movies.models import Movie, Ticket


class ListMoviesViewTest(django_test.TestCase):
    VALID_MOVIE_DATA = {
        'title': 'Avatar',
        'image': SimpleUploadedFile(name='test_image.jpg',
                                    content=open(r"C:\Users\PC\Pictures\Softuni Cinema Project Photos\spider-man.jpg",
                                                 'rb').read(), content_type='image/jpeg'),
        'trailer_video': 'https://www.youtube.com/watch?v=zAH-GjT4Jpw',
        'genre': 'Adventure',
        'year': '2010',
        'description': 'Ben-10 The Movie.',
        'duration': '140',
        'category': 'B',
    }

    def test_get__when_correct_template_given__expect_success(self):
        response = self.client.get(reverse('list movies'))

        self.assertTemplateUsed(response, 'movies/list_movies.html')

    def test_get__when_incorrect_template_given__expect_fail(self):
        response = self.client.get(reverse('list movies'))

        self.assertTemplateNotUsed(response, 'movies/add_movie.html')

    def test_get__when_two_movies_created__expect_context_to_contain_two_movies(self):
        movies_to_create = (
            Movie(**self.VALID_MOVIE_DATA),
            Movie(title='Test',
                  image=self.VALID_MOVIE_DATA['image'],
                  trailer_video=self.VALID_MOVIE_DATA['trailer_video'],
                  genre=self.VALID_MOVIE_DATA['genre'],
                  year=self.VALID_MOVIE_DATA['year'],
                  description=self.VALID_MOVIE_DATA['description'],
                  duration=self.VALID_MOVIE_DATA['duration'],
                  category=self.VALID_MOVIE_DATA['category'],
                  ),
        )

        Movie.objects.bulk_create(movies_to_create)

        response = self.client.get(reverse('list movies'))


        movies = response.context['object_list']


        self.assertEqual(len(movies), 2)


    def test_get__when_no_movies_created__expect_context_to_contain_no_movies(self):
        response = self.client.get(reverse('list movies'))


        movies = response.context['object_list']


        self.assertEqual(len(movies), 0)


class AddMovieViewTests(django_test.TestCase):
    VALID_MOVIE_DATA = {
        'title': 'Avatar',
        'image': SimpleUploadedFile(name='test_image.jpg',
                                    content=open(r"C:\Users\PC\Pictures\Softuni Cinema Project Photos\spider-man.jpg",
                                                 'rb').read(), content_type='image/jpeg'),
        'trailer_video': 'https://www.youtube.com/watch?v=zAH-GjT4Jpw',
        'genre': 'Adventure',
        'year': '2010',
        'description': 'Ben-10 The Movie.',
        'duration': '140',
        'category': 'B',
        'price': '15',
    }

    def test_get__load_correct_template(self):
        response = self.client.get(reverse('add movie'))

        self.assertTemplateUsed(response, 'movies/add_movie.html')

    def test_post__create_new_movie_and_ticket_to_the_movie_and_redirect(self):
        response = self.client.post(
            reverse('add movie'),
            data=self.VALID_MOVIE_DATA,
        )

        movie = Movie.objects.first()
        ticket = Ticket.objects.first()

        # test if redirect works
        expected_url = reverse('list movies')
        self.assertRedirects(response, expected_url)

        self.assertIsNotNone(movie)
        self.assertIsNotNone(ticket)

    # def test_post__if_redirect_works(self):
    #     response = self.client.post(
    #         reverse('add movie'),
    #         data=self.VALID_MOVIE_DATA,
    #     )
    #
    #     # test if redirect works
    #     expected_url = reverse('list movies')
    #     self.assertRedirects(response, expected_url)


    def test_get__ticket_form_in_context(self):
        response = self.client.get(reverse('add movie'))
        ticket_form = response.context['ticket_form']
        self.assertIsNotNone(ticket_form)