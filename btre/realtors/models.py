from django.db import models
from django.utils import timezone
# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='realtors/%Y/%m/%d')
    description = models.TextField()
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return self.name
