from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:pack_id>', views.checkout, name='checkout'),
    path('create_checkout_session/<int:pack_id>', views.create_checkout_session, name='create_checkout_session'),
]
