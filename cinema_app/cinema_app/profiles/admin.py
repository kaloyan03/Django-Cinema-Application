from django.contrib import admin

# Register your models here.
from cinema_app.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'user']


admin.site.register(Profile, ProfileAdmin)