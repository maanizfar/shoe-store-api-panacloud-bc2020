# Generated by Django 3.0.7 on 2020-06-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200630_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_in_inventory',
            field=models.BooleanField(default=True),
        ),
    ]