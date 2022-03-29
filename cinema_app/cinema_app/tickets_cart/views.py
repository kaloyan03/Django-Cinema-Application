from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator

from cinema_app.movies.models import Ticket
from cinema_app.settings import EMAIL_HOST_USER

@method_decorator(login_required, name='dispatch')
def cart_view(request):
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
            ticket.cart_item_id = item.id
            tickets.append(ticket)

    if request.method == 'POST':
        send_email(request.user.email, tickets, total_price, total_quantity)
        cart.cart.delete()
        return redirect('list movies')

    context = {
        'cart': cart,
        'tickets': tickets,
        'total_price': total_price,
        'total_quantity': total_quantity,
    }
    return render(request, 'checkout_cart.html', context)

@method_decorator(login_required, name='dispatch')
def add_to_cart(request, id, quantity):
    ticket = Ticket.objects.get(id=id)
    cart = Cart(request)
    cart.add(ticket, ticket.price, quantity)
    return redirect('cart view')

@method_decorator(login_required, name='dispatch')
def remove_from_cart(request, id):
    cart = Cart(request)
    items = cart.cart.item_set.all()
    # vvv doing that this way without filter, because Cart doesn't have manager vvv
    item = [i for i in items if i.id == id][0]
    ticket = Ticket.objects.get(id=item.object_id)
    current_item_quantity = item.quantity
    item_price = item.unit_price
    cart.update(ticket, current_item_quantity - 1, item_price)
    return redirect('cart view')

@method_decorator(login_required, name='dispatch')
def send_email(email, tickets, total_price, total_quantity):
    subject = 'Thank you for your order'
    message = '\n'.join([
        f'{ticket.movie.title} with duration {ticket.movie.duration} minutes on price {ticket.price}$'
        for ticket in tickets])
    message += '\n'
    message += f'There is total quantity for your order: {total_quantity}$.\n'
    message += f'There is total price for your order: {total_price}$.'
    recipient = email
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
