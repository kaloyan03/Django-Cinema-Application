from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views, View
# Create your views here.
from django.utils.decorators import method_decorator

from cinema_app.movies.forms import AddProjectionForm
from cinema_app.projections.models import Projection


@method_decorator(staff_member_required, name='dispatch')
class AddProjection(views.CreateView):
    model = Projection
    template_name = 'movies/../../templates/projections/add_projection.html'
    success_url = reverse_lazy('movie details')
    form_class = AddProjectionForm


def show_movie_projections(request, day, movie_id):
    projections_that_day = Projection.objects.order_by('time').filter(day_of_the_week=day)
    movie_projections_that_day = []

    for projection in projections_that_day:
        [movie_projections_that_day.append(projection) for ticket in projection.ticket.all() if
         movie_id == ticket.movie.id]

    for projection in movie_projections_that_day:
        movie_ticket = projection.ticket.filter(movie_id=movie_id)[0]
        projection.movie_ticket = movie_ticket

    context = {
        'projections': movie_projections_that_day,
        'day': day,
    }
    return render(request, 'projections/show_projections.html', context)

# class ShowMovieProjections(views.ListView):
#     model = Projection
#     context_object_name = 'projections'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
