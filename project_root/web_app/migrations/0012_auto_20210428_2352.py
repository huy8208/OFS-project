# Generated by Django 3.0.14 on 2021-04-28 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0011_auto_20210425_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Vegetable', 'Vegetable'), ('Fruit', 'Fruit'), ('Meat', 'Meat'), ('Pantry', 'Pantry'), ('Dairy', 'Dairy'), ('Frozen Foods', 'Frozen Foods'), ('Beverages', 'Beverages')], max_length=200, null=True),
        ),
    ]
