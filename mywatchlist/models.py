from django.db import models

# Create your models here.
class watchlistmovie(models.Model):
    watched = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    release_date = models.TextField()
    review = models.TextField()