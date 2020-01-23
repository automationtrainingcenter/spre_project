from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/%y/%m/%d', default='')
    description = models.TextField()
    email = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name
