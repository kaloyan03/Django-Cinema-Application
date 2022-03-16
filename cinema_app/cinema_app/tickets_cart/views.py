from cart.cart import Cart
from django.shortcuts import render
from django.views import generic as views

# Create your views here.

class ShowCartView(views.TemplateView):
    model = Cart
    template_name = 'checkout_cart.html'


class AddToCartView(views.CreateView):
    model = Cart
    template_name = 'movies/movie_details.html'
    fields = '__all__'