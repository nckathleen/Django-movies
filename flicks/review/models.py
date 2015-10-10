from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=255)


class Rater(models.Model):
    gender = models.CharField(max_length=1)
    user = models.OneToOneField(null=True)


class Ratings(models.Model):
    movie_id = models.ForeignKey(Movie)
    rater_id = models.ForeignKey(Rater)
