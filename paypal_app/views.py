from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import uuid
def home(request):
    host=request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '20',

        'item_name': 'product 1',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request,'paypal_app/home.html',{'form':form})
def payment_done(request):
    messages.success(request,'you just made a payment')
    return redirect('/')
def payment_cancelled(request):
    messages.error(request,'you just made cancelled this payment')
    return redirect('/')