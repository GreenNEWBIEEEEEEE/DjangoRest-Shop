# Generated by Django 3.1.4 on 2020-12-27 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Merchandises', '0003_auto_20201226_0235'),
        ('Includes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='include',
            name='merchandiseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Merchandises.merchandise', verbose_name='merchandise'),
        ),
    ]