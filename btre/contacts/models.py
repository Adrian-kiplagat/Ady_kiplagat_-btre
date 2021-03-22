from django.db import models
from django.utils import timezone
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField(blank=True)
    contact_date = models.DateField(default=timezone.now)
    user_id = models.IntegerField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
