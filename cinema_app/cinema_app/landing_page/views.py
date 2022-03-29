from django.shortcuts import render

# Create your views here.
from django.views import View
from star_ratings.models import Rating

from cinema_app.movies.models import Movie


class ShowLandingPage(View):
    def get(self, request):
        "  TODO filter top 3 rated movies  "
        top_ratings = Rating.objects.order_by('-average')[:3]
        top_movies_ids = [r.object_id for r in top_ratings]
        top_movies = []

        for movie in Movie.objects.all():
            if movie.id in top_movies_ids:
                movie.stars_average = Rating.objects.get(object_id=movie.id).average
                top_movies.append(movie)

        context = {
            'movies': top_movies,
            'user_is_staff': True if request.user.is_staff else False
        }

        return render(request, 'landing_page.html', context)