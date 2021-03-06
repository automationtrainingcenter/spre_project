from django.db import models
from realtors.models import Realtor
from datetime import datetime

# id: INT
# realtor: INT (FOREIGN KEY [realtor])


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.today)
    photo_main = models.ImageField(upload_to="media/%y/%m/%d")
    photo_1 = models.ImageField(upload_to="media/%y/%m/%d", blank=True)
    photo_2 = models.ImageField(upload_to="media/%y/%m/%d", blank=True)
    photo_3 = models.ImageField(upload_to="media/%y/%m/%d", blank=True)
    photo_4 = models.ImageField(upload_to="media/%y/%m/%d", blank=True)
    photo_5 = models.ImageField(upload_to="media/%y/%m/%d", blank=True)
    photo_6 = models.ImageField(upload_to="media/%y/%m/%d", blank=True)

    def __str__(self):
        return self.title
