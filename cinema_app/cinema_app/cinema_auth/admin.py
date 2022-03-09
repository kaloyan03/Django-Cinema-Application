from django.contrib import admin

# Register your models here.
from cinema_app.cinema_auth.models import CinemaUser

admin.site.register(CinemaUser)