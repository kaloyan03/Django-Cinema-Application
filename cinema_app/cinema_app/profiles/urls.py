from django.urls import path

from cinema_app.profiles.views import ShowProfileView

urlpatterns = (
    path('<int:pk>', ShowProfileView.as_view(), name='profile'),
)