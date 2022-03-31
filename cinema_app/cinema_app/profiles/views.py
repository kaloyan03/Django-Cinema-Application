from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

# Create your views here.
from cinema_app.profiles.forms import ProfileForm, EditProfileForm
from cinema_app.profiles.models import Profile

UserModel = get_user_model()


@method_decorator(login_required, name='dispatch')
class ShowProfileView(views.TemplateView):
    model = Profile
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.filter(user=user)
        context['profile'] = profile[0]
        return context


@method_decorator(login_required, name='dispatch')
class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'profile/delete_profile.html'
    success_url = reverse_lazy('sign in')

    def form_valid(self, form):
        user = self.request.user
        user.delete()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'profile'

class CompleteProfileView(views.CreateView):
    model = UserModel
    template_name = 'profile/complete_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        kwargs = self.get_form_kwargs()
        user = kwargs['user']
        user.has_completed_profile = True
        user.save()
        return super().form_valid(form)