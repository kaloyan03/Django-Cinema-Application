from django.urls import path

from cinema_app.actors.views import ListActors

urlpatterns = (
    path('', ListActors.as_view(), name='list actors'),
)