# Generated by Django 3.1.4 on 2020-12-30 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0006_auto_20201226_0232'),
        ('Orders', '0006_auto_20201229_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='memberID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.member', verbose_name='Test'),
        ),
    ]
