from django.urls import path

from cinema_app.landing_page.views import ShowLandingPage

urlpatterns = (
    path('', ShowLandingPage.as_view(), name='landing page'),
)