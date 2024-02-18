from django.db import models

# Create your models here.
class Url(models.Model):
    long = models.TextField(unique=True)
    short = models.TextField(unique=True)
    short_viewed = models.IntegerField(default=0)

