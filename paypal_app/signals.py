from django.shortcuts import get_object_or_404
from .models import Order
from paypal.standard.ipn.signals import valid_ipn_received,invalid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def valid_ipn(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        new_order=Order(paid=True)
        new_order.save()

@receiver(invalid_ipn_received)
def invalid_ipn(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        new_order=Order(paid=True)
        new_order.save()

