# Generated by Django 3.1.4 on 2020-12-21 08:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('coupon_code', models.IntegerField(blank=True, db_column='Coupon_Code', null=True)),
                ('merchandise_id', models.IntegerField(db_column='Merchandise_id')),
                ('shipping_type', models.CharField(db_column='Shipping_Type', max_length=45)),
                ('payment_type', models.CharField(db_column='Payment_Type', max_length=45)),
                ('status', models.CharField(db_column='Status', max_length=45)),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('total_price', models.IntegerField(db_column='Total_Price')),
                ('date', models.DateTimeField(db_column='Date', default=datetime.datetime.now)),
                ('memberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.member', verbose_name='MemberID')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
