from django.urls import path

from django.contrib.auth import views as auth_views
from cinema_app.cinema_auth.views import SignInView, SignUpView, SignOutView, ResetPasswordView, ResetPasswordSentView, \
    ResetPasswordConfirmView, ResetPasswordCompleteView

# URLs for the auth app
urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_sent/', ResetPasswordSentView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),
)