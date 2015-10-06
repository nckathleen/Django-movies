from django.db import models


class Rater(models.Model):
    pass
    # rater =    models.SmallIntegerField()
    # movie = models.ForeignKey(Movie)
    # rating = models.SmallIntegerField()
    #
    # def __str__(self):
    #     return self.rater


class Movie(models.Model):
    #movie = models.ForeignKey()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.FloatField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    # def rating_count(self):
    #     return self.rating_set.count()
