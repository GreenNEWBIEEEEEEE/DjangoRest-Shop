# Generated by Django 3.1.4 on 2021-06-06 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0011_auto_20210607_0404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount_price',
        ),
    ]
