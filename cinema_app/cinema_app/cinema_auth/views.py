from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from cinema_app.cinema_auth.forms import SignUpForm, SignInForm, ResetPasswordForm, PasswordSetForm


class SignUpView(View):
    """
    GET request - rendering the page(using Django Templates) with form(SignUpForm).
    POST request - If form is valid - creating user(saving the form) and signing in directly. Redirecting to "http://localhost:8000/movies"(list movies).
    """

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


class SignInView(views.LoginView):
    """
        GET request - rendering the page(using Django Templates) with form(SignInForm).
        POST request - If form is valid - signing in the user. Redirecting to "http://localhost:8000/movies"(list movies).

    """
    template_name = 'auth/sign_in.html'
    next_page = reverse_lazy('list movies')
    form_class = SignInForm


class SignOutView(views.LogoutView):
    """
    Signing the user out and redirecting to sign in page.
    """
    next_page = reverse_lazy('sign in')


class ResetPasswordView(views.PasswordResetView):
    """
        GET request - rendering the page(using Django Templates) with form(ResetPasswordForm).
        POST request - Sending email with link for password reset(if email exists). Redirecting to the "http://localhost:8000/auth/reset_password_sent/"(password_reset_done)
    """
    template_name = 'auth/password_reset.html'
    form_class = ResetPasswordForm


class ResetPasswordSentView(views.PasswordResetDoneView):
    """
        GET request - rendering the page(using Django Templates) with information to check your email.
    """
    template_name = 'auth/password_reset_sent.html'


class ResetPasswordConfirmView(views.PasswordResetConfirmView):
    """
           GET request - rendering the page(using Django Templates) with form(PasswordSetForm).
           POST request - If form is valid - changing the user password. Redirecting to the "http://localhost:8000/auth/reset_password_complete/"(password_reset_complete)
       """
    template_name = 'auth/password_reset_form.html'
    form_class = PasswordSetForm


class ResetPasswordCompleteView(views.PasswordResetCompleteView):
    """
    GET request - rendering the page(using Django Templates) with information that the user password is changed.
    """

    template_name = 'auth/password_reset_complete.html'
