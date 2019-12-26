from django.db import models


# Create your models here.


class Standard(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    std_year = models.DateField(unique_for_year=4)
    note = models.CharField(max_length=255)

