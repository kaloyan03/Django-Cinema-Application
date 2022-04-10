from django.contrib import admin

# Register your models here.
from cinema_app.movies.models import Movie, Projections, Ticket


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'year', 'description', 'duration', 'category']


admin.site.register(Movie, MovieAdmin)


class ProjectionsAdmin(admin.ModelAdmin):
    list_display = ['id','time']
    filter_horizontal = ['movie']


admin.site.register(Projections, ProjectionsAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ['price', 'movie']


admin.site.register(Ticket, TicketAdmin)