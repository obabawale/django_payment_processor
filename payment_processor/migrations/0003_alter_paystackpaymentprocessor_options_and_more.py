# Generated by Django 5.0.6 on 2024-06-30 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_processor', '0002_rename_paystactpaymentprocessor_paystackpaymentprocessor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paystackpaymentprocessor',
            options={'managed': True, 'verbose_name': 'Paystack', 'verbose_name_plural': 'Paystack'},
        ),
        migrations.AlterModelOptions(
            name='stripepaymentprocessor',
            options={'managed': True, 'verbose_name': 'Stripe', 'verbose_name_plural': 'Stripe'},
        ),
        migrations.AlterModelTable(
            name='paystackpaymentprocessor',
            table='payment_processor_paystack',
        ),
        migrations.AlterModelTable(
            name='stripepaymentprocessor',
            table='payment_processor_stripe',
        ),
    ]
