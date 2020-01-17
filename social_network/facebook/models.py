from django.db import models


# Create your models here.
class FacebookUser(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    friends = models.ManyToManyField("self", blank=True, null=True, default=None)


class Photos(models.Model):
    name = models.CharField(max_length=100)
    likes = models.ManyToManyField(FacebookUser, null=True, blank=True, default=None)


class Videos(models.Model):
    name = models.CharField(max_length=100)
    size = models.FloatField()
    likes = models.ManyToManyField(FacebookUser, null=True, blank=True, default=None)
