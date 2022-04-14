from django.urls import path

from cinema_app.projections import views

urlpatterns = [
    path('<str:day>/<int:movie_id>/', views.show_movie_projections, name='show projections'),
]