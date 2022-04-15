from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

# Create your views here.
from cinema_app.profiles.decorators import profile_required
from cinema_app.profiles.forms import ProfileForm, EditProfileForm
from cinema_app.profiles.models import Profile

UserModel = get_user_model()


# Added custom decorator for profile required. To access this page you must be logged in and with completed profile.
@method_decorator(login_required, name='dispatch')
@method_decorator(profile_required, name='dispatch')
class ShowProfileView(views.TemplateView):
    """
        GET request - rendering the page(using Django Templates) with information for the profile and edit, delete operations..
    """
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
    """
    GET request - rendering the page(using Django Templates) confirmation for the profile deleting.
    POST request - deleting profile and UserModel linked to that profile in DB if form is valid. Redirecting to "http://localhost:8000/auth/sign-in" (sign in).
    """
    model = Profile
    template_name = 'profile/delete_profile.html'
    success_url = reverse_lazy('sign in')

    # deleting UserModel linked to profile
    def form_valid(self, form):
        user = self.request.user
        user.delete()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditProfileView(views.UpdateView):
    """
        GET request - rendering the page(using Django Templates) with form(EditProfileForm).
        POST request - edit profile if form is valid. Redirecting to "http://localhost:8000/profile/" (profile).
        """
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'profile'

@method_decorator(login_required, name='dispatch')
class CompleteProfileView(views.CreateView):
    """
            GET request - rendering the page(using Django Templates) with form(ProfileForm).
            POST request - create user profile if form is valid. Redirecting to "http://localhost:8000/profile/" (profile).
            """
    model = UserModel
    template_name = 'profile/complete_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    # pass the user to the form init.
    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # attach has_completed_profile to the user, with which nav link to profile will redirect to the show profile, not complete profile.
    def form_valid(self, form):
        kwargs = self.get_form_kwargs()
        user = kwargs['user']
        user.has_completed_profile = True
        user.save()
        return super().form_valid(form)
