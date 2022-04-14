from django.shortcuts import render

# Create your views here.
from django.views import View
from star_ratings.models import Rating

from cinema_app.movies.models import Movie


class ShowLandingPage(View):
    """
    GET request - rendering the page(using Django Templates).
    On this page will be top 3 rated movies( if there is movies rated ).
    On each movie container there will be details button for all users, including the no-authenticated.
    For the staff users or superuser there will be edit button and delete button on each movie.
    Details button redirecting to "http://localhost:8000/movies/<int:id>/", (movie details, <id>)"
    Edit button redirecting to "http://localhost:8000/movies/edit/<int:id>/", (edit movie, <id>)"
    Delete button redirecting to "http://localhost:8000/movies/delete/<int:id>/", (delete movie, <id>)"
    """
    def get(self, request):
        "  TODO filter top 3 rated movies  "
        top_ratings = Rating.objects.order_by('-average')[:3]
        top_movies_ids = [r.object_id for r in top_ratings]
        top_movies = []

        # attach average star rating on top rated movies.
        for movie in Movie.objects.all():
            if movie.id in top_movies_ids:
                movie.stars_average = Rating.objects.get(object_id=movie.id).average
                top_movies.append(movie)

        # if user is staff there is edit and delete buttons
        context = {
            'movies': top_movies,
            'user_is_staff': True if request.user.is_staff else False
        }

        return render(request, 'landing_page.html', context)