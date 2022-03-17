from cart.cart import Cart
from django.shortcuts import render

# Create your views here.
from cinema_app.movies.models import Ticket, Movie


def show_cart(request):
    cart = Cart(request)
    items = cart.cart.item_set.all()

    counter = 0
    tickets = []

    for ticket in Ticket.objects.all():
        if ticket.id == items[counter].object_id:
            ticket.quantity = items[counter].quantity
            ticket.total_price = items[counter].total_price
            tickets.append(ticket)
        counter += 1

    context = {
        'cart': cart,
        'tickets': tickets,
    }
    return render(request, 'checkout_cart.html', context)


def add_to_cart(request, id, quantity):
    ticket = Ticket.objects.get(id=id)
    cart = Cart(request)
    cart.add(ticket, ticket.price, quantity)