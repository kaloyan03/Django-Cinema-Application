from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from cinema_app.movies.forms import AddMovieForm, EditMovieForm, AddTicketForm
from cinema_app.movies.models import Movie, Ticket


class ListMovies(views.ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 3
    template_name = 'movies/list_movies.html'


class AddMovie(views.CreateView):
    model = Movie
    form_class = AddMovieForm
    template_name = 'movies/add_movie.html'
    success_url = reverse_lazy('list movies')

    def form_valid(self, form):
        movie = form.save()
        ticket_price = self.get_form_kwargs()['data']['price']
        ticket = Ticket(movie=movie, price=ticket_price)
        ticket.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket_form = AddTicketForm()
        context['ticket_form'] = ticket_form
        return context
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
    template_name = 'movies/edit_movie.html'



class MovieDetails(views.DetailView):
    model = Movie
    template_name = 'movies/movie_details.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        ticket = Ticket.objects.get(movie_id=movie.id)
        context['ticket'] = ticket
        return context
