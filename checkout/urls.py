from django.urls import path
from . import views

from .views import webhook

urlpatterns = [
    path('checkout/<int:pack_id>', views.checkout, name='checkout'),
    path('create_checkout_session/<int:pack_id>',
         views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('wh/', webhook, name='webhook'),
]
