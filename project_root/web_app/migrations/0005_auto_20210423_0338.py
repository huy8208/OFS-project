# Generated by Django 3.0.14 on 2021-04-23 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20210423_0309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_superuser',
        ),
    ]