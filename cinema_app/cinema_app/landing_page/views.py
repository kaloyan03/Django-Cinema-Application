from django.shortcuts import render

# Create your views here.
from django.views import View

from cinema_app.movies.models import Movie


class ShowLandingPage(View):
    def get(self, request):
        "TODO filter top 3 liked movies"
        movies = Movie.objects.all()[:3]
        context = {
            'movies': movies,
        }

        return render(request, 'landing_page.html', context)