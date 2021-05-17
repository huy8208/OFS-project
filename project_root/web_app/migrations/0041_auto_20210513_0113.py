# Generated by Django 3.0.14 on 2021-05-13 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0040_merge_20210512_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_product', to='web_app.Product'),
        ),
    ]