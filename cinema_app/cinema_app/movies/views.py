from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from star_ratings.models import Rating

from cinema_app.movies.forms import AddMovieForm, EditMovieForm, AddTicketForm, AddCommentForm
from cinema_app.movies.models import Movie, Ticket, Comment
from cinema_app.projections.models import Projection


class ListMovies(views.ListView):
    """
        GET request - rendering the page(using Django Templates).
        On this page will be listed all movies( if there is movies ), with pagination 3 movies on page.
        On each movie container there will be details button for all users, including the no-authenticated.
        For the staff users or superuser there will be edit button and delete button on each movie.
        Details button redirecting to "http://localhost:8000/movies/<int:id>/", (movie details, <id>)"
        Edit button redirecting to "http://localhost:8000/movies/edit/<int:id>/", (edit movie, <id>)"
        Delete button redirecting to "http://localhost:8000/movies/delete/<int:id>/", (delete movie, <id>)"
        """
    model = Movie
    context_object_name = 'movies'
    queryset = Movie.objects.all()
    paginate_by = 3
    template_name = 'movies/list_movies.html'

    # Add movies average rating to the queryset, object lists
    def get_queryset(self):
        movies = super().get_queryset()

        for movie in movies:
            try:
                current_movie_average_rating = Rating.objects.get(object_id=movie.id).average
                movie.average_rating = current_movie_average_rating
            except:
                movie.average_rating = 'Not rated yet'

        return movies

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # if user is staff there is edit and delete buttons
        context['user_is_staff'] = True if self.request.user.is_staff else False
        return context


@method_decorator(staff_member_required, name='dispatch')
class AddMovie(views.FormView):
    """
        GET request - rendering the page(using Django Templates) with forms(AddMovieForm and AddTicketForm).
        POST request - creating movie in DB if form is valid. Redirecting to "http://localhost:8000/movies"(list movies).
    """

    def form_invalid(self, form):
        return form

    def get(self, request, *args, **kwargs):
        movie_form = AddMovieForm()
        ticket_form = AddTicketForm()

        context = {
            'movie_form': movie_form,
            'ticket_form': ticket_form,
        }

        return render(request, 'movies/add_movie.html', context)

    def post(self, request, *args, **kwargs):
        movie_form = AddMovieForm(request.POST, request.FILES)
        ticket_form = AddTicketForm(request.POST)

        context = {
            'movie_form': movie_form,
            'ticket_form': ticket_form,
        }

        if movie_form.is_valid() and ticket_form.is_valid():
            movie = movie_form.save()
            Ticket.objects.create(movie=movie, price=ticket_form.cleaned_data['price'])

            return redirect('list movies')

        return render(request, 'movies/add_movie.html', context)


@method_decorator(staff_member_required, name='dispatch')
class EditMovie(views.UpdateView):
    """
        GET request - rendering the page(using Django Templates) with forms(EditMovieForm).
        POST request - editing movie if form is valid. Redirecting to "http://localhost:8000/movies/<int:id>"(movie details, <id>)
    """
    model = Movie
    form_class = EditMovieForm
    context_object_name = 'movie'
    template_name = 'movies/edit_movie.html'

    def get_success_url(self, **kwargs):
        movie = self.object
        return reverse_lazy('movie details', kwargs={'pk': movie.pk})


class MovieDetails(views.DetailView):
    """
            GET request - rendering the page(using Django Templates) where is information to the selected movie.
        """

    model = Movie
    template_name = 'movies/movie_details.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        # getting ticket from the movie object and adding it to the context
        ticket = Ticket.objects.get(movie_id=movie.id)
        context['ticket'] = ticket
        # adding comment form and comments (if any ) to the context.
        comment_form = AddCommentForm()
        context['comment_form'] = comment_form
        comments = Comment.objects.filter(movie=movie)
        context['comments'] = comments
        # getting movie screenings from the ticket and filtering them.
        movie_projections = Projection.objects.filter(ticket=ticket)
        if movie_projections:
            movie_projection_days = [projection.day_of_the_week for projection in movie_projections]
            projection_days_no_repeating = self.get_no_repeating_projection_days(movie_projection_days)
            projection_days_sorted = self.sort_days_of_the_week(projection_days_no_repeating)
            context['movie_projection_days'] = projection_days_sorted
        return context

    # this method filters the days that are not repeating: ['Monday', 'Monday'] - It returns you ['Monday']
    @staticmethod
    def get_no_repeating_projection_days(days):
        no_repeating_days = []
        for day in days:
            if day not in no_repeating_days:
                no_repeating_days.append(day)
        return no_repeating_days

    # this method sorts the days of the week:  ['Tuesday', 'Monday'] - It returns you ['Monday', 'Tuesday]
    @staticmethod
    def sort_days_of_the_week(days_unsorted):
        days_of_the_week_correct_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return sorted(days_unsorted, key=days_of_the_week_correct_order.index)


@method_decorator(staff_member_required, name='dispatch')
class DeleteMovie(views.DeleteView):
    """
            GET request - rendering the page(using Django Templates) with confirmation on the deleting.
            POST request - deleting the movie with the ticket. Redirecting to "http://localhost:8000/movies"(list movies).
        """
    model = Movie
    template_name = 'movies/delete_movie.html'
    success_url = reverse_lazy('list movies')

    def form_valid(self, form):
        movie = self.object
        ticket = Ticket.objects.get(movie_id=movie.id)
        ticket.delete()
        return super().form_valid(form)


# This FBV is created to post comments
def comment_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = AddCommentForm(request.POST)

    if form.is_valid():
        comment = Comment(
            movie=movie,
            user_id=request.user.id,
            comment=form.cleaned_data['comment'],
        )

        comment.save()
    return redirect('movie details', movie.id)
