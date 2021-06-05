from django.db import models
from datetime import datetime
from Members.models import Member
# Create your models here.
from django.contrib.auth import get_user_model
from Coupons.models import Coupon
User = get_user_model()

class Order(models.Model):
    coupon_code = models.OneToOneField(Coupon, on_delete = models.CASCADE , blank=True, null=True)  # Field name made lowercase.
    shipping_type = models.CharField(db_column='Shipping_Type', max_length=45)  # Field name made lowercase.
    payment_type = models.CharField(db_column='Payment_Type', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    total_price = models.IntegerField(db_column='Total_Price')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', default=datetime.now)  # Field name made lowercase.
    memberID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Member")
    #discount_price = models.IntegerField(db_column='Discount_Price')  # Field name made lowercase.
    class Meta:
        db_table = 'Orders'
