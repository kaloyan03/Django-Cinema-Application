from django.urls import path

from cinema_app.profiles.views import ShowProfileView, CompleteProfileView, DeleteProfileView

urlpatterns = (
    path('', ShowProfileView.as_view(), name='profile'),
    path('complete_profile/', CompleteProfileView.as_view(), name='complete profile'),
    path('delete/<int:pk>', DeleteProfileView.as_view(), name='delete profile'),
)