from datetime import datetime
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import Sum, F

from cinema_app.movies.models import Ticket
from cinema_app.projections.models import Projection


UserModel = get_user_model()

# class CartManager(models.Manager):
#     """
#     Manager for Cart model.
#     If UserModel has existing Cart
#     """
#     def new_or_get(self, request):
#         cart_id = request.session.get("cart_id", None)
#         qs = self.get_queryset().filter(id=cart_id)
#         if qs.count() == 1:
#             new_obj = False
#             cart_obj = qs.first()
#             if request.user.is_authenticated() and cart_obj.user is None:
#                 cart_obj.user = request.user
#                 cart_obj.save()
#         else:
#             cart_obj = Cart.objects.new(user=request.user)
#             new_obj = True
#             request.session['cart_id'] = cart_obj.id
#         return cart_obj, new_obj
#
#
#     def new(self, user=None):
#         user_obj = None
#         if user is not None:
#             if user.is_authenticated():
#                 user_obj = user
#         return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    """
    This model represents Cart in DB.
    It consists of
    user(fk to UserModel),
    tickets(ManyToMany to Ticket),
    updated(when is last update),
    it has property that calculates total price.
    """
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    tickets = models.ManyToManyField(
        Ticket,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    # objects = CartManager

    @property
    def total_price(self):
        return self.item_set.aggregate(
            total_price=Sum(F('quantity') * F('ticket__price'))
        )['total_price'] or Decimal('0')


class Item(models.Model):
    """
        This model represents Item in DB.
        It consists of
        ticket(fk to Ticket),
        projection(fk to Projection),
        cart(fk to Cart),
        quantity(of tickets in cart)
        """
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
    )

    projection = models.ForeignKey(
        Projection,
        on_delete=models.CASCADE,
        default=1,
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(

    )





