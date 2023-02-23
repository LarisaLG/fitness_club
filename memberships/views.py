from django.shortcuts import render
from .models import Package, PackDetail

# Create your views here.


def package_price(request):
    """
    This view renders to the user the packages prices page.
    """
    package_price = Package.objects.all()
    context = {
        'package_price': package_price
        }
    return render(request, 'memberships/packages.html', context)
