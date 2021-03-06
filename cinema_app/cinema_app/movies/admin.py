from django.contrib import admin

# Register your models here.
from cinema_app.movies.models import Movie, Ticket, Comment


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'year', 'description', 'duration', 'category']


admin.site.register(Movie, MovieAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ['price', 'movie']


admin.site.register(Ticket, TicketAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user']


admin.site.register(Comment, CommentAdmin)


