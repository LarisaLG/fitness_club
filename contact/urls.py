from django.urls import path
# from .views import ContactView
from . import views

urlpatterns = [
    path('contacts/', views.contact, name='contact'),
]


# urlpatterns = [
#     path('', ContactView.as_view(), name='contact'),
# ]
