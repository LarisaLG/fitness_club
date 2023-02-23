from django.shortcuts import render
from .models import *

# Create your views here.


def package_price(request):
    """
    This view renders to the user the packages prices page.
    """
    price = Package.objects.all()
    context = {
           'price': price
        }
    return render(request, 'memberships/packages.html', context)
