from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.core import mail

from cinema_app.movies.models import Movie, Ticket
from cinema_app.projections.models import Projection
from cinema_app.tickets_cart.models import Cart, Item

VALID_MOVIE_DATA = {
    'title': 'Avatar',
    'image': SimpleUploadedFile(name='test_image.jpg',
                                content=open(r"C:\Users\PC\Pictures\Softuni Cinema Project Photos\spider-man.jpg",
                                             'rb').read(), content_type='image/jpeg'),
    'trailer_video': 'https://www.youtube.com/watch?v=zAH-GjT4Jpw',
    'genre': 'Adventure',
    'year': 2010,
    'description': 'Ben-10 The Movie.',
    'duration': 140,
    'category': 'B',
}

VALID_PROJECTION_DATA = {
    'day_of_the_week': 'Monday',
    'time': '18:00',
}

USER_CREDENTIALS = {
    'email': 'testtest@abv.bg',
    'password': '1312231321qwe',
}

UserModel = get_user_model()


class CartViewTests(django_test.TestCase):
    def setUp(self) -> None:
        movie = Movie.objects.create(**VALID_MOVIE_DATA)
        ticket = Ticket.objects.create(movie=movie, price=15)
        projection = Projection.objects.create(day_of_the_week=VALID_PROJECTION_DATA['day_of_the_week'],
                                               time=VALID_PROJECTION_DATA['time'])
        projection.ticket.add(ticket)
        UserModel.objects.create_user(**USER_CREDENTIALS)
        self.client.login(**USER_CREDENTIALS)

    def test_get__context__expect_to_have_tickets_total_price_total_quantity(self):
        user = UserModel.objects.first()
        ticket = Ticket.objects.first()
        cart = Cart.objects.get(user=user)
        projection = Projection.objects.first()
        Item.objects.create(ticket=ticket, cart=cart, quantity=1, projection=projection)

        response = self.client.get(reverse('cart view'))
        ticket = response.context['tickets'][0]
        total_price = response.context['total_price']
        total_quantity = response.context['total_quantity']

        self.assertIsNotNone(ticket)
        # test ticket attributes that are added
        self.assertIsNotNone(ticket.quantity)
        self.assertIsNotNone(ticket.total_price)
        self.assertIsNotNone(ticket.item_id)
        # end

        self.assertIsNotNone(total_price)
        self.assertIsNotNone(total_quantity)

    def test_post__expect_to_delete_item_and_send_mail(self):
        user = UserModel.objects.first()
        ticket = Ticket.objects.first()
        cart = Cart.objects.get(user=user)
        projection = Projection.objects.first()
        Item.objects.create(ticket=ticket, cart=cart, quantity=1, projection=projection)

        self.client.post(reverse('cart view'))

        item = Item.objects.first()
        self.assertIsNone(item)
        self.assertEqual(len(mail.outbox), 1)


class AddToCartTests(django_test.TestCase):
    def setUp(self) -> None:
        movie = Movie.objects.create(**VALID_MOVIE_DATA)
        ticket = Ticket.objects.create(movie=movie, price=15)
        projection = Projection.objects.create(day_of_the_week=VALID_PROJECTION_DATA['day_of_the_week'],
                                               time=VALID_PROJECTION_DATA['time'])
        projection.ticket.add(ticket)
        UserModel.objects.create_user(**USER_CREDENTIALS)
        self.client.login(**USER_CREDENTIALS)

    def test_post__add_ticket_to_cart__expect_ticket_to_be_added(self):
        self.client.post(reverse('add to cart', kwargs={
            'ticket_id': Ticket.objects.first().id,
            'quantity': 1,
            'projection_id': Projection.objects.first().id,
        }))

        cart = Cart.objects.first()
        items_in_cart = cart.item_set.all()

        self.assertIsNotNone(items_in_cart)


class RemoveFromCartTests(django_test.TestCase):
    def setUp(self) -> None:
        movie = Movie.objects.create(**VALID_MOVIE_DATA)
        ticket = Ticket.objects.create(movie=movie, price=15)
        projection = Projection.objects.create(day_of_the_week=VALID_PROJECTION_DATA['day_of_the_week'],
                                               time=VALID_PROJECTION_DATA['time'])
        projection.ticket.add(ticket)
        UserModel.objects.create_user(**USER_CREDENTIALS)
        self.client.login(**USER_CREDENTIALS)

    def test_post__remove_ticket_from_cart__expect_ticket_to_be_removed(self):
        self.client.post(reverse('add to cart', kwargs={
            'ticket_id': Ticket.objects.first().id,
            'quantity': 1,
            'projection_id': Projection.objects.first().id,
        }))

        item = Cart.objects.first().item_set.first()

        self.client.post(reverse('remove from cart', kwargs={
            'id': item.id,
        }))

        cart = Cart.objects.first()
        items_in_cart = cart.item_set.all()

        self.assertEqual(items_in_cart[0].quantity, 0)
