from typing import Any
from django.db import models
from .utils.payment_processors import ShoppingCartService


class Cart(models.Model):

    cart_total = models.FloatField(verbose_name="Cart Total")
    paid = models.BooleanField(name="Paid", default=False)

    class Meta:
        db_table = 'shopping_cart'
        managed = True
        verbose_name = 'ShoppingCart'
        verbose_name_plural = 'ShoppingCarts'


class PaymentProcessor(models.Model):

    name = models.CharField(verbose_name="Name", max_length=16)
    processor_key = models.CharField(verbose_name="Acquirer", max_length=16)

    @classmethod
    def process_payment(cls, processor_key: str, cart: Cart):
        return ShoppingCartService(processor_key).checkout(cart)

    class Meta:
        db_table = 'payment_processor__payment_processor'
        managed = True
        verbose_name = 'Payment Processor'
        verbose_name_plural = 'Payment Processors'