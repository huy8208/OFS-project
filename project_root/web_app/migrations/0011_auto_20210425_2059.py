# Generated by Django 3.0.14 on 2021-04-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0010_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_images/'),
        ),
    ]
