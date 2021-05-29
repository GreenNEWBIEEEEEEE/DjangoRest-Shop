from django.db import models
from Merchandises.models import Merchandise
from Orders.models import Order
# Create your models here.

class Include(models.Model):
    merchandiseID = models.ForeignKey(Merchandise, on_delete=models.CASCADE, verbose_name='merchandise')
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='orderID')
    Quantity = models.IntegerField('Quantity', default=0)
    class Meta:
        db_table = 'Includes'
