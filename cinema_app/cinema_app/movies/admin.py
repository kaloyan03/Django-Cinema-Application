from django.contrib import admin

# Register your models here.
from cinema_app.movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'year', 'description', 'duration', 'category']


admin.site.register(Movie, MovieAdmin)