from django.db import models


class Rater(models.Model):
    pass


class Movie(models.Model):
    # movie = models.ForeignKey()
    title = models.CharField(max_length=255)

    def rating_count(self):
        return self.rating_set.count()

    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.FloatField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return 'The rating for {} is {}.'.format(self.movie, self.rating)
