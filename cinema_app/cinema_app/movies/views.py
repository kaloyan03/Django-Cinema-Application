from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from cinema_app.movies.models import Movie


class ListMovies(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'list_movies.html'

class AddMovie(CreateView):
    model = Movie
    fields = '__all__'
    template_name = 'add_movie.html'
    success_url = reverse_lazy('list movies')
