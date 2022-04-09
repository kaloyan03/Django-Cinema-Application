from django.contrib import admin

# Register your models here.
from cinema_app.tickets_cart.models import Cart, Item


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    filter_horizontal = ['tickets']


admin.site.register(Cart, CartAdmin)



class ItemAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'ticket']


admin.site.register(Item, ItemAdmin)