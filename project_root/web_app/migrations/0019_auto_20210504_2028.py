# Generated by Django 3.0.14 on 2021-05-04 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0018_auto_20210504_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='address2',
        ),
    ]