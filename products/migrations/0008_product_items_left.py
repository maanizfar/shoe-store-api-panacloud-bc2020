# Generated by Django 3.0.7 on 2020-07-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200630_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='items_left',
            field=models.PositiveIntegerField(default=3),
        ),
    ]
