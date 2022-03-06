from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ShowLandingPage(TemplateView):
    template_name = 'landing_page.html'