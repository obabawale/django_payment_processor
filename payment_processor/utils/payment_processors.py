from abc import ABC, abstractmethod


class Cart():
    def __init__(self, amount):
        self.amount = amount


class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(cart: Cart):
        return NotImplementedError

    class Meta:
        abstract = True


class StripePaymentProcessor(PaymentProcessor):
    def process_payment(cart: Cart):
        print("Processing Payment With Stripe")
        return super().process_payment()


class PaystackPaymentProcessor(PaymentProcessor):
    def process_payment(cart: Cart):
        print("Processing Payment With Paystack")
        return super().process_payment()


class ShoppingCartService():

    def init(self, payment_processor):
        self.payment_processor = payment_processor

    def checkout(self, cart: Cart):
        self.payment_processor.process_payment(
            cart)  # run process payment fuction
