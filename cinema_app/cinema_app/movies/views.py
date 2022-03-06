from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from cinema_app.movies.models import Movie


class ListMovies(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'list_movies.html'