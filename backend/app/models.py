from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# class Itinerary(models.Model):
    


class Package(models.Model):
    name = models.CharField(max_length=150)
    itinerary = JSONField(null=True,blank=True)
    listPrice = models.FloatField()
    mrp = models.FloatField()
    duration = models.IntegerField()
    sightseeing = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    best_time = models.CharField(max_length=100)
    overview = models.TextField()
    inclusion = models.TextField()
    exclusion = models.TextField()
    cancellation_policy = models.TextField()
    tnc = models.TextField()
    state = models.CharField(max_length=100)
    # itnery =:

    def __str__(self):
        return self.name



    
