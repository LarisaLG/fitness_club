from django.shortcuts import render, reverse, redirect
from memberships.models import Package

# Create your views here.


def checkout(request):
    pack_details = PackDetail.objects.get()
    context = {
        'pack': pack_details
    }
    return render(request, 'checkout/checkout.html', context)
