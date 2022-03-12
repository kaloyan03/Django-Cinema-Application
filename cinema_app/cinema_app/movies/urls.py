from django.urls import path

from cinema_app.movies.views import ListMovies, AddMovie, EditMovie

urlpatterns = (
    path('', ListMovies.as_view(), name='list movies'),
    path('add/', AddMovie.as_view(), name='add movie'),
    path('edit/<int:pk>', EditMovie.as_view(), name='edit movie'),
)