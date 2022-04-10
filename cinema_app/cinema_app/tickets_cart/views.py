from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator

from cinema_app.movies.models import Ticket, Projection
from cinema_app.settings import EMAIL_HOST_USER

@login_required
def cart_view(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    items = cart.item_set.all()
    items_tickets_id = [item.ticket_id for item in items]

    total_price = cart.total_price
    total_quantity = sum([i.quantity for i in items])

    tickets = []

    for ticket in Ticket.objects.all():
        if ticket.id in items_tickets_id:
            item_index = items_tickets_id.index(ticket.id)
            item_id = items[item_index].ticket_id
            item = [i for i in items if i.ticket_id == item_id][0]
            if item.quantity == 0:
                item.delete()
                break
            ticket.quantity = item.quantity
            ticket.total_price = item.ticket.price * item.quantity
            ticket.item_id = item.id
            ticket.projection= item.projection
            tickets.append(ticket)

    if request.method == 'POST':
        send_email(request.user.email, tickets, total_price, total_quantity)

        cart_items = cart.item_set.all()
        for item in cart_items:
            item.delete()

        return redirect('list movies')

    context = {
        'cart': cart,
        'tickets': tickets,
        'total_price': total_price,
        'total_quantity': total_quantity,
    }
    return render(request, 'auth/../../templates/tickets_cart/cart_view.html', context)

from cinema_app.tickets_cart.models import Cart, Item


@login_required
def add_to_cart(request, ticket_id, quantity, projection_id):
    ticket = Ticket.objects.get(id=ticket_id)
    projection = Projection.objects.get(id=projection_id)
    if request.method == 'POST':
        user = request.user
        cart = Cart.objects.get(user=user)

        cart_items_ticket_ids = [item.ticket_id for item in Item.objects.filter(cart=cart)]

        if ticket.id not in cart_items_ticket_ids:
            Item.objects.create(
                ticket=ticket,
                quantity=quantity,
                projection=projection,
                cart=cart,
            )
        else:
            item = Item.objects.get(ticket=ticket, cart=cart)
            item.quantity += quantity
            item.save()

        return redirect('cart view')

    else:
        context = {
            'projection': projection,
            'ticket': ticket,
        }

        return render(request, 'tickets_cart/add_to_cart.html', context)

@login_required
def remove_from_cart(request, id):
    item = Item.objects.get(id=id)
    item.quantity -= 1
    item.save()
    return redirect('cart view')

def send_email(email, tickets, total_price, total_quantity):
    subject = 'Thank you for your order'
    message = '\n'.join([
        f'Ticket for {ticket.movie.title} with duration {ticket.movie.duration} minutes at {ticket.projection.time.strftime("%H:%M")} on price {ticket.price:.2f}$'
        for ticket in tickets])
    message += '\n'
    message += f'There is total tickets for your order: {total_quantity}.\n'
    message += f'There is total price for your order: {total_price:.2f}$.'
    recipient = email
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
