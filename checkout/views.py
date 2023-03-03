from django.conf import settings
from django.shortcuts import render, reverse, redirect
from memberships.models import *

import stripe

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


# stripe.api_key = 'sk_test_51MMAu7HLOnIV8WXaMwf21i2mljQXvmka2DRJkKFW9fSGTOSPAj9TWq4b8Tu8mvGLOv56PiSua94xmnSS3RVLgBvj00cl6Hrien'
stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request, pack_id):

    package = Package.objects.get(id=pack_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': package.title,
                },
                'unit_amount_decimal': package.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/cancel',
       )

    return redirect(session.url, code=303)
