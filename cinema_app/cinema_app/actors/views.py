from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from cinema_app.actors.models import Actor


class ListActors(ListView):
    model = Actor
    template_name = 'list_actors.html'
    context_object_name = 'actors'