from django.contrib import admin

# Register your models here.
from cinema_app.projections.models import Projection


class ProjectionsAdmin(admin.ModelAdmin):
    list_display = ['id','time', 'day_of_the_week']
    filter_horizontal = ['movie']


admin.site.register(Projection, ProjectionsAdmin)