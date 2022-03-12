from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from cinema_app.movies.forms import AddMovieForm
from cinema_app.movies.models import Movie


class ListMovies(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'list_movies.html'


class AddMovie(View):
    # model = Movie
    # form_class = AddMovieForm
    # template_name = 'add_movie.html'
    # success_url = reverse_lazy('list movies')
    #
    # def form_invalid(self, form):
    #     return form

    def get(self, request):
        form = AddMovieForm()

        context = {
            'form': form,
        }

        return render(request, 'add_movie.html', context)

    def post(self, request):
        form = AddMovieForm(request.POST)

        context = {
            'form': form,
        }

        if form.is_valid():
            form.save()
            return redirect('list movies')

        return render(request, 'add_movie.html', context)