from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

# Create your views here.
from cinema_app.profiles.forms import ProfileForm
from cinema_app.profiles.models import Profile


class ShowProfileView(views.CreateView):
    model = Profile
    template_name = 'profile.html'
    form_class = ProfileForm



    def get_context_data(self, **kwargs):
        user = self.request.user
        profile = Profile.objects.filter(user=user)
        context = super().get_context_data(**kwargs)
        context['profile'] = profile[0]
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        url = self.request.path
        return url