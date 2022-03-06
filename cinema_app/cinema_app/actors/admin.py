from django.contrib import admin

# Register your models here.
from cinema_app.actors.models import Actor


class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'country']


admin.site.register(Actor, ActorAdmin)

