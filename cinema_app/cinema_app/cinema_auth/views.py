from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from cinema_app.cinema_auth.forms import SignUpForm, SignInForm, ResetPasswordForm


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


class SignInView(views.LoginView):
    template_name = 'auth/sign_in.html'
    next_page = reverse_lazy('list movies')
    form_class = SignInForm




class SignOutView(views.LogoutView):
    next_page = reverse_lazy('sign in')


class ResetPasswordView(views.PasswordResetView):
    template_name = 'auth/password_reset.html'


class ResetPasswordSentView(views.PasswordResetDoneView):
    template_name = 'auth/password_reset_sent.html'


class ResetPasswordConfirmView(views.PasswordResetConfirmView):
    template_name = 'auth/password_reset_form.html'


class ResetPasswordCompleteView(views.PasswordResetCompleteView):
    template_name = 'auth/password_reset_complete.html'
