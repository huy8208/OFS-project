# Generated by Django 3.0.14 on 2021-05-10 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0037_shippingaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
