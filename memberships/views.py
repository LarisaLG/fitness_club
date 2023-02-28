from django.shortcuts import render
from .models import Package, PackDetail
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def package_price(request):
    """
    This view renders to the user the packages prices page.
    """
    package_price = Package.objects.all()
    pack_details = PackDetail.objects.all()
    context = {
        'packages': package_price,
        'pack_details': pack_details
        }
    return render(request, 'memberships/packages.html', context)
