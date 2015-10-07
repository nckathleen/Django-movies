from django.db import models


class Rater(models.Model):
    # id is automatic

    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNKNOWN, 'Unknown'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.id


class Movie(models.Model):
    # movie = models.ForeignKey()
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('rating'))['rating_avg']

    def rating_count(self):
        return self.rating_set.count()

    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return 'User {} gave {} {} stars.'\
            .format(self.rater, self.movie, self.rating)
