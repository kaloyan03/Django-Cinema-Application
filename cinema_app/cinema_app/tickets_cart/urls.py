from django.urls import path

from cinema_app.tickets_cart.views import show_cart, add_to_cart

urlpatterns = (
    path('', show_cart, name='show cart'),
    path('add/<int:id>/<int:quantity>', add_to_cart, name='add to cart'),
)