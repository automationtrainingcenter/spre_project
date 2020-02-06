from django.db import models
from datetime import datetime

# Create your models here.


class contact(models.Model):
    user_id = models.IntegerField()
    listing = models.CharField(max_length=50)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=5000)
    contact_date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name
