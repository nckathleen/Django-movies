from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Rater(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'

    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('UNKNOWN', 'Unknown'))

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # user = models.OneToOneField(null=True)

    def __str__(self):
        return self.id


class Rating(models.Model):
    stars = models.PositiveSmallIntegerField()
    movie = models.ForeignKey(Movie)
    rating = models.ForeignKey(Rater)

    def __str__(self):
        return self.stars

#
# def load_ml_data():
#
#     import csv
#     import json
#
#     # read movie data into fixtures
#     movies = []
#     with open (ml-m1/movies.dat, encoding='Windows-1252') as f:
#         reader = csv.reader()
#         for x in f:
#             print()
