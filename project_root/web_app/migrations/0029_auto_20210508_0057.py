# Generated by Django 3.0.14 on 2021-05-08 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0028_merge_20210507_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_in_cart', to='web_app.Order'),
        ),
    ]
