from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django import test as django_test

from cinema_app.movies.models import Movie


class MovieModelTest(django_test.TestCase):
    VALID_MOVIE_DATA = {
        'title': 'Avatar',
        'image': SimpleUploadedFile(name='test_image.jpg', content=open(r"C:\Users\PC\Pictures\Softuni Cinema Project Photos\spider-man.jpg", 'rb').read(), content_type='image/jpeg'),
        'trailer_video': 'https://www.youtube.com/watch?v=zAH-GjT4Jpw',
        'genre': 'Adventure',
        'year': '2010',
        'description': 'Ben-10 The Movie.',
        'duration': '140',
        'category': 'B',
    }

    def test_movie_create__when_everything_is_valid__expect_success(self):
        movie = Movie(**self.VALID_MOVIE_DATA)
        movie.save()
        self.assertIsNotNone(movie.pk)


    def test_movie_create__when_title_start_with_lower_letter__expect_fail(self):
        movie = Movie(
            title='avatar',
            image=self.VALID_MOVIE_DATA['image'],
            trailer_video=self.VALID_MOVIE_DATA['trailer_video'],
            genre=self.VALID_MOVIE_DATA['genre'],
            year=self.VALID_MOVIE_DATA['year'],
            description=self.VALID_MOVIE_DATA['description'],
            duration=self.VALID_MOVIE_DATA['duration'],
            category=self.VALID_MOVIE_DATA['category'],
        )

        with self.assertRaises(ValidationError) as error_message:
            movie.full_clean()
            movie.save()

        self.assertIsNotNone(error_message)