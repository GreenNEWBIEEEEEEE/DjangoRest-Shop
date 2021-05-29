from django.db import models
from Members.models import Member
# Create your models here.
class Coupon(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, default="ABCD123", max_length=150)  # Field name made lowercase.
    type = models.FloatField(db_column='Type', max_length=45, default=0)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=300)  # Field name made lowercase.
    available = models.BooleanField(db_column='Available', default=True)  # Field name made lowercase.

    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="memberID", default="")
    class Meta:
        db_table = 'coupon'
    def __str__(self):
        return self.code
