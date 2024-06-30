from django.contrib import admin
from .models import Cart, StripePaymentProcessor, PaystackPaymentProcessor

# Register your models here.
admin.site.register(Cart)
admin.site.register(StripePaymentProcessor)
admin.site.register(PaystackPaymentProcessor)
