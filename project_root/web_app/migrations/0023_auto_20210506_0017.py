# Generated by Django 3.0.14 on 2021-05-06 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0022_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(default=models.CharField(max_length=200, null=True), max_length=200),
        ),
    ]
