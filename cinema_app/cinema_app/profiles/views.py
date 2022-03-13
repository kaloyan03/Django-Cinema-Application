from django.shortcuts import render
from django.views import generic as views

# Create your views here.
from cinema_app.profiles.models import Profile


class ShowProfileView(views.CreateView):
    model = Profile
    template_name = 'profile.html'



    def get_context_data(self, **kwargs):
        context = kwargs
        user = self.request.user
        profile = Profile.objects.filter(user=user)
        context['profile'] = profile
        return context