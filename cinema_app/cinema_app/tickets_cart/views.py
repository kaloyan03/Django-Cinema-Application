from cart.cart import Cart
from django.shortcuts import render, redirect

# Create your views here.
from cinema_app.movies.models import Ticket, Movie


def show_cart(request):
    cart = Cart(request)
    items = cart.cart.item_set.all()
    items_ids = [item.object_id for item in items]

    total_price = sum([i.total_price for i in items])
    total_quantity = sum([i.quantity for i in items])


    tickets = []

    for ticket in Ticket.objects.all():
        if ticket.id in items_ids:
            item_index = items_ids.index(ticket.id)
            item_id = items[item_index].object_id
            item = [i for i in items if i.object_id == item_id][0]
            ticket.quantity = item.quantity
            ticket.total_price = item.total_price
            tickets.append(ticket)

            # if counter == len(items):
            #     break
            #
            # if ticket.id == items[counter].object_id:
            #     ticket.quantity = items[counter].quantity
            #     ticket.total_price = items[counter].total_price
            #     tickets.append(ticket)
            # counter += 1

    context = {
        'cart': cart,
        'tickets': tickets,
        'total_price': total_price,
        'total_quantity': total_quantity,
    }
    return render(request, 'checkout_cart.html', context)


def add_to_cart(request, id, quantity):
    ticket = Ticket.objects.get(id=id)
    cart = Cart(request)
    cart.add(ticket, ticket.price, quantity)
    return redirect('show cart')
