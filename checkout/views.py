from django.shortcuts import render, reverse, redirect
from memberships.models import *

# Create your views here.


def checkout(request, pack_id):
    """
    This view renders to the user the checkout page or
    redirects to login page if user not logged in.
    """
    if request.user.is_authenticated:
        package = Package.objects.get(id=pack_id)
        pack_details = PackDetail.objects.all()
        context = {
            'package': package,
            'pack': pack_details
        }
        return render(request, 'checkout/checkout.html', context)
    else:
        return redirect('../accounts/login')
