# Generated by Django 3.1.4 on 2020-12-27 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Merchandises', '0003_auto_20201226_0235'),
        ('Members', '0006_auto_20201226_0232'),
        ('Carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='memberID',
        ),
        migrations.AddField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(default=0, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='cart',
            name='member',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Members.member', verbose_name='memberID'),
        ),
        migrations.AddField(
            model_name='cart',
            name='merchandise',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Merchandises.merchandise', verbose_name='merchandiseID'),
        ),
    ]
