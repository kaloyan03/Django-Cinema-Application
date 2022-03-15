from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from cinema_app.cinema_auth.forms import SignUpForm, SignInForm
from cinema_app.cinema_auth.models import CinemaUser


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()

        context = {
            'form': form,
        }

        return render(request, 'auth/sign_up.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list movies')

        context = {
            'form': form,
        }
        return render(request, 'auth/sign_up.html', context)

# class SignUp(CreateView):
#     template_name = 'sign_up.html'
#     form_class = SignUpForm
#     success_url = reverse_lazy('list movies')


class SignInView(LoginView):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm




class SignOutView(LogoutView):
    next_page = reverse_lazy('sign in')