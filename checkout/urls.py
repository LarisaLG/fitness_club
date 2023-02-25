from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:pack_id>', views.checkout, name='checkout'),
]
