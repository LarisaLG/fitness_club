from django.urls import path
from . import views

urlpatterns = [
    path('packages/', views.package_price, name='packages'),
]
