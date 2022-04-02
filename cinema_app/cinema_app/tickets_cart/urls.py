from django.urls import path

# from cinema_app.tickets_cart.views import cart_view, add_to_cart, remove_from_cart
#
# urlpatterns = (
#     path('', cart_view, name='cart view'),
#     path('add/<int:id>/<int:quantity>/', add_to_cart, name='add to cart'),
#     path('remove/<int:id>/', remove_from_cart, name='remove from cart'),
# )
from cinema_app.tickets_cart.views import add_to_cart, cart_view, remove_from_cart

urlpatterns = (
    path('', cart_view, name='cart view'),
    path('add/<int:id>/<int:quantity>/', add_to_cart, name='add to cart'),
    path('remove/<int:id>/', remove_from_cart, name='remove from cart'),
)
