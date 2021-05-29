# Generated by Django 3.1.4 on 2020-12-29 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coupons', '0004_auto_20201229_1426'),
        ('Orders', '0005_auto_20201228_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon_code',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Coupons.coupon'),
        ),
    ]
