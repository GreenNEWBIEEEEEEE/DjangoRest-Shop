# Generated by Django 3.1.4 on 2020-12-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0005_auto_20201226_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=200, verbose_name='密碼'),
        ),
    ]
