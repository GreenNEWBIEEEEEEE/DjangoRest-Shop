# Generated by Django 3.1.4 on 2020-12-29 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0006_auto_20201226_0232'),
        ('Coupons', '0003_auto_20201221_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='memberID',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='order',
        ),
        migrations.AddField(
            model_name='coupon',
            name='member',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Members.member', verbose_name='memberID'),
        ),
    ]
