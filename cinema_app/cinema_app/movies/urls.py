from django.urls import path

from cinema_app.movies.views import ListMovies

urlpatterns = (
    path('', ListMovies.as_view(), name='list movies'),
)