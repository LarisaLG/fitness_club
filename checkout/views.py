from django.conf import settings
from django.shortcuts import render, reverse, redirect
from memberships.models import *
from django.views.decorators.csrf import csrf_exempt
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


stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request, pack_id):
    YOUR_DOMAIN = 'http://127.0.0.1:8000'
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
        success_url=YOUR_DOMAIN + '/checkout/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/cancel',
       )

    return redirect(session.url, code=303)


def success(request):
    session_id = request.GET.get('session_id')
    context = {'session_id': session_id}
    return render(request, 'checkout/success.html', context)


def cancel(request):
    return render(request, 'checkout/cancel.html')


@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
            handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
