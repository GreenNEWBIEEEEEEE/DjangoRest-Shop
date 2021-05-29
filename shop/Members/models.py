from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Member(AbstractUser):
    #username = None
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []
    username = models.CharField("會員姓名", max_length=20, unique=True, default="")
    nickname = models.CharField("會員暱稱", max_length=20)
    phone = models.CharField("電話號碼", max_length=10)
    address = models.CharField("地址", max_length=100)
    email = models.EmailField(('email address'), unique=True)
    password = models.CharField("密碼", max_length=200)
    activated = models.BooleanField("驗證狀態", default=False)
    class Meta:
        db_table = 'Members'

    def __str__(self):
        return self.username


