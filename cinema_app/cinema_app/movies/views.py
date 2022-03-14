from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from cinema_app.movies.forms import AddMovieForm, EditMovieForm
from cinema_app.movies.models import Movie


class ListMovies(views.ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'list_movies.html'


class AddMovie(views.CreateView):
    model = Movie
    form_class = AddMovieForm
    template_name = 'add_movie.html'
    success_url = reverse_lazy('list movies')
    #
    # def form_invalid(self, form):
    #     return form

    # def get(self, request):
    #     form = AddMovieForm()
    #
    #     context = {
    #         'form': form,
    #     }
    #
    #     return render(request, 'add_movie.html', context)
    #
    # def post(self, request):
    #     form = AddMovieForm(request.POST)
    #
    #     context = {
    #         'form': form,
    #     }
    #
    #     if form.is_valid():
    #         form.save()
    #         return redirect('list movies')
    #
    #     return render(request, 'add_movie.html', context)


class EditMovie(views.UpdateView):
    model = Movie
    success_url = reverse_lazy('list movies')
    form_class = EditMovieForm
    context_object_name = 'movie'
    template_name = 'edit_movie.html'


class MovieDetails(views.DetailView):
    model = Movie
    template_name = 'movie_details.html'
    context_object_name = 'movie'