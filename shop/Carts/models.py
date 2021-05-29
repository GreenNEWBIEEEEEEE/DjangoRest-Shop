from django.db import models
from Members.models import Member
from Merchandises.models import Merchandise
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()
class Cart(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='memberID', default="")
    merchandise = models.ForeignKey(Merchandise, on_delete=models.CASCADE, verbose_name='merchandiseID', default="")
    Quantity = models.IntegerField('Quantity', default=0)
    total_price = models.IntegerField('total_price', default=0)
    class Meta:
        db_table = 'cart'

        '''
    def save(self, *args, **kwargs):
        self.total_price = self.merchandise.price * self.Quantity
        super(Cart, self).save(*args, **kwargs)
        '''
        '''
        product = Merchandise.objects.get(name=self.merchandise)
        self.total_price = product.price * self.Quantity
        super(Cart, self).save(*args, **kwargs)
        '''


