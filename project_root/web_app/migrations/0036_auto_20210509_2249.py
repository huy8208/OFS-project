# Generated by Django 3.0.14 on 2021-05-09 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0035_auto_20210509_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
