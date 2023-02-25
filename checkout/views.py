from django.shortcuts import render, reverse, redirect
from memberships.models import *

# Create your views here.


def checkout(request, pack_id):
    package = Package.objects.get(id=pack_id)
    pack_details = PackDetail.objects.all()
    context = {
        'package': package,
        'pack': pack_details
    }
    return render(request, 'checkout/checkout.html', context)
