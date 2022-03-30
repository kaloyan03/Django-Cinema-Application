from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse, reverse_lazy
from star_ratings.models import Rating

from cinema_app.movies.models import Movie, Ticket, Comment

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

UserModel = get_user_model()

class ListMoviesViewTest(django_test.TestCase):
    def setUp(self) -> None:
        Movie.objects.create(**VALID_MOVIE_DATA)
        Ticket.objects.create(price=15, movie=Movie.objects.first())
        Rating.objects.create(average=5.0, count=1, total=5, object_id=Movie.objects.first().id, content_type_id=7)

    def test_get__when_correct_template_given__expect_success(self):
        response = self.client.get(reverse('list movies'))

        self.assertTemplateUsed(response, 'movies/list_movies.html')

    def test_get__when_incorrect_template_given__expect_fail(self):
        response = self.client.get(reverse('add movie'))

        self.assertTemplateNotUsed(response, 'movies/list_movies.html')

    def test_get__when_two_movies_created__expect_context_to_contain_two_movies(self):
        # delete the one movie that is created in setUp
        Movie.objects.first().delete()

        movies_to_create = (
            Movie(**VALID_MOVIE_DATA),
            Movie(title='Test',
                  image=VALID_MOVIE_DATA['image'],
                  trailer_video=VALID_MOVIE_DATA['trailer_video'],
                  genre=VALID_MOVIE_DATA['genre'],
                  year=VALID_MOVIE_DATA['year'],
                  description=VALID_MOVIE_DATA['description'],
                  duration=VALID_MOVIE_DATA['duration'],
                  category=VALID_MOVIE_DATA['category'],
                  ),
        )

        Movie.objects.bulk_create(movies_to_create)

        response = self.client.get(reverse('list movies'))

        movies = response.context['object_list']

        self.assertEqual(len(movies), 2)

    def test_get__when_no_movies_created__expect_context_to_contain_no_movies(self):
        response = self.client.get(reverse('list movies'))

        movies = response.context['object_list']
        # Not equal, because in setUp I created one movie
        self.assertNotEqual(len(movies), 0)

    def test_get__get_queryset_movies__expect_movie_objects_to_have_rating(self):
        response = self.client.get(reverse('list movies'))

        movie = response.context['object_list'][0]

        self.assertEqual(movie.average_rating, 5.000)

    def test_get__if_user_is_staff__expect_is_staff_to_be_true(self):
        USER_CREDENTIALS = {
            'email': 'testtest@abv.bg',
            'password': '1312231321qwe',
            'is_staff': True,
        }

        UserModel.objects.create_user(**USER_CREDENTIALS)
        self.client.login(**USER_CREDENTIALS)
        response = self.client.get(reverse('list movies'))
        is_staff = response.context['user_is_staff']

        self.assertEqual(is_staff, True)


class AddMovieViewTests(django_test.TestCase):
    VALID_MOVIE_AND_TICKET_DATA = {
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

    def setUp(self) -> None:
        USER_CREDENTIALS = {
            'email': 'testtest@abv.bg',
            'password': '1312231321qwe',
            'is_staff': True,
        }

        UserModel.objects.create_user(**USER_CREDENTIALS)
        self.client.login(**USER_CREDENTIALS)

    def test_get__load_correct_template(self):
        response = self.client.get(reverse('add movie'))

        self.assertTemplateUsed(response, 'movies/add_movie.html')

    def test_post__create_new_movie_and_ticket_to_the_movie_and_redirect(self):
        response = self.client.post(
            reverse('add movie'),
            data=self.VALID_MOVIE_AND_TICKET_DATA,
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

    def test_get__if_user_is_staff__expect_is_staff_to_be_true(self):
        response = self.client.get(reverse('add movie'))
        user = response.context['user']
        self.assertEqual(user.is_staff, True)

class EditMovieViewTest(django_test.TestCase):
    def setUp(self) -> None:
        Movie.objects.create(**VALID_MOVIE_DATA)
        Ticket.objects.create(price=15, movie=Movie.objects.first())

        USER_CREDENTIALS = {
            'email': 'testtest@abv.bg',
            'password': '1312231321qwe',
            'is_staff': True,
        }

        UserModel.objects.create_user(**USER_CREDENTIALS)
        self.client.login(**USER_CREDENTIALS)

    def test_get__when_correct_template_given__expect_correct_template(self):
        movie = Movie.objects.first()
        response = self.client.get(reverse('edit movie', kwargs={'pk': movie.pk}))

        self.assertTemplateUsed(response, 'movies/edit_movie.html')

    def test_get__when_incorrect_template_given__expect_incorrect_template(self):
        response = self.client.get(reverse('add movie'))

        self.assertTemplateNotUsed(response, 'movies/edit_movie.html')

    def test_post__when_edit_movie__expect_to_edit_the_movie(self):
        movie = Movie.objects.first()
        response = self.client.post(reverse_lazy('edit movie', kwargs={'pk': movie.pk}), {
            'title': 'Test edit',
            'image': VALID_MOVIE_DATA['image'],
            'trailer_video': VALID_MOVIE_DATA['trailer_video'],
            'genre': VALID_MOVIE_DATA['genre'],
            'year': VALID_MOVIE_DATA['year'],
            'description': VALID_MOVIE_DATA['description'],
            'duration': VALID_MOVIE_DATA['duration'],
            'category': VALID_MOVIE_DATA['category'],
        })

        #         check the status code
        self.assertEqual(response.status_code, 200)

        #         check if movie title is changed

        updated_movie = response.context['movie']

        self.assertEqual(updated_movie.title, 'Test edit')

    def test_get__if_user_is_staff__expect_is_staff_to_be_true(self):
        response = self.client.get(reverse('list movies'))
        is_staff = response.context['user_is_staff']

        self.assertEqual(is_staff, True)


class MovieDetailsViewTest(django_test.TestCase):
    def setUp(self) -> None:
        Movie.objects.create(**VALID_MOVIE_DATA)
        Ticket.objects.create(price=15, movie=Movie.objects.first())

    def test_get__when_correct_template_given__expect_correct_template(self):
        movie = Movie.objects.first()
        response = self.client.get(reverse('movie details', kwargs={'pk': movie.pk}))

        self.assertTemplateUsed(response, 'movies/movie_details.html')

    def test_get__when_incorrect_template_given__expect_incorrect_template(self):
        response = self.client.get(reverse('add movie'))

        self.assertTemplateNotUsed(response, 'movies/details.html')

    def test_get__correct_context_data__expect_ticket_and_comments_with_form(self):
        movie = Movie.objects.first()

        response = self.client.get(reverse('movie details', kwargs={'pk': movie.pk}))

        ticket = response.context['ticket']
        comment_form = response.context['comment_form']
        comments = response.context['comments']

        self.assertIsNotNone(ticket)
        self.assertIsNotNone(comment_form)
        self.assertIsNotNone(comments)


class DeleteMovieViewTests(django_test.TestCase):
    def setUp(self) -> None:
        Movie.objects.create(**VALID_MOVIE_DATA)
        Ticket.objects.create(price=15, movie=Movie.objects.first())

        USER_CREDENTIALS = {
            'email': 'testtest@abv.bg',
            'password': '1312231321qwe',
            'is_staff': True,
        }

        UserModel.objects.create_user(**USER_CREDENTIALS)
        self.client.login(**USER_CREDENTIALS)

    def test_get__when_correct_template_given__expect_correct_template(self):
        movie = Movie.objects.first()
        response = self.client.get(reverse('delete movie', kwargs={'pk': movie.pk}))

        self.assertTemplateUsed(response, 'movies/delete_movie.html')

    def test_get__when_incorrect_template_given__expect_incorrect_template(self):
        response = self.client.get(reverse('add movie'))

        self.assertTemplateNotUsed(response, 'movies/delete_movie.html')

    def test_post__delete_movie__expect_to_delete_movie(self):
        movie = Movie.objects.first()

        self.client.post(reverse('delete movie', kwargs={'pk': movie.pk}))

        movies = Movie.objects.all()

        self.assertEqual(len(movies), 0)

    def test_post__delete_movie__expect_to_delete_ticket(self):
        movie = Movie.objects.first()

        self.client.post(reverse('delete movie', kwargs={'pk': movie.pk}))

        tickets = Ticket.objects.all()

        self.assertEqual(len(tickets), 0)

    def test_get__if_user_is_staff__expect_is_staff_to_be_true(self):
        response = self.client.get(reverse('list movies'))
        is_staff = response.context['user_is_staff']

        self.assertEqual(is_staff, True)


class CommentMovieTest(django_test.TestCase):
    def setUp(self) -> None:
        Movie.objects.create(**VALID_MOVIE_DATA)
        Ticket.objects.create(price=15, movie=Movie.objects.first())

    def test_post__comment_movie__expect_movie_to_have_comment(self):
        USER_CREDENTIALS = {
            'email': 'testtest@abv.bg',
            'password': '1312231321qwe',
        }

        UserModel.objects.create_user(**USER_CREDENTIALS)

        movie = Movie.objects.first()
        Comment.objects.create(movie=movie, comment='test comment', user_id=UserModel.objects.first().id)

        self.assertIsNotNone(movie.comment_set.all())


