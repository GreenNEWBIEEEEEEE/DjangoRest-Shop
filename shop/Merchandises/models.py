from django.db import models

# Create your models here.

class Merchandise(models.Model):
    name = models.CharField("name", max_length=100)
    price = models.IntegerField("price", default=0)
    detail_info = models.CharField("產品描述", max_length=500)
    deleted = models.BooleanField("是否被刪除", default=False)
    image = models.ImageField(upload_to="", null=True, blank=True, verbose_name="封面圖")
    launched = models.BooleanField("是否發售中", default=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Merchandises'

