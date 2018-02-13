from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        # Charge the user's card:
        charge = stripe.Charge.create(
            amount=999,
            currency="usd",
            description="Example charge",
            source=token,
        )
    context = {'publishKey': publishKey}
    template = 'checkout.html'
    return render(request, template, context)
