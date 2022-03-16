from django.urls import path
from cinema_app.tickets_cart import views

urlpatterns = (
    path('cart/', views.ShowCartView.as_view(), name='show cart'),
    path('add-to-cart/', views.AddToCartView.as_view(), name='add to cart'),
)