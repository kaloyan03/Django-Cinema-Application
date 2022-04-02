from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from cinema_app.tickets_cart.models import Cart

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(
            user=instance,
        )