from django.conf import settings
from django.contrib.auth.models import User
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
#    zipcode = models.CharField(max_length=5)
#    age = models.PositiveIntegerField()
#    occupation = models.CharField(max_length=40)

    def __str__(self):
        return self.id

#
# class Profile(models.Model):
#     # user = User.objects.create_user()
#     user = models.OneToOneField(User)
#
#     def __unicode__(self):
#         return self.user.get_rater()
    # def load_fake_data():
    #     '''Create some fake users'''
    #     from faker import Faker
    #
    #     fake = Faker()
    #
    #     users = []
    #     for _ in range(50):
    #         new_user = User(
    #             username=fake.user_name(),
    #             email=fake.email(),
    #             password=fake.password())
    #         new_user.save()
    #         users.append(new_user)


class Movie(models.Model):
    # movie = models.ForeignKey()
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('rating'))['rating_avg']

    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return 'User {} gave {} {} stars.'\
            .format(self.rater, self.movie, self.rating)


class Profile(models.Model):
    # user = User.objects.create_user()
    user = models.OneToOneField(User, primary_key=True)



def load_ml_data():

    import csv
    import json

    # Code used to import files for Movies, Ratings, and Raters.
    users = []

    with open('ml-1m/users.dat') as f:

        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split(
                                    '::'),
                                delimiter='\t')
        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'moviedb.Rater',
                'pk': int(row['UserID'])
            }

            users.append(user)

    with open('users.json', 'w') as f:   # place to dump/put the data
        f.write(json.dumps(users))

    movies = []

    with open('ml-1m/movies.dat', encoding='Windows-1252') as f:

        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title'.split('::'),
                                delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title'],
                },
                'model': 'moviedb.Movie',
                'pk': int(row['MovieID'])
            }

            movies.append(movie)

    with open('movies.json', 'w') as f:   # place to dump/put the data
        f.write(json.dumps(movies))

    ratings = []

    with open('ml-1m/ratings.dat', encoding='Windows-1252') as f:

        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating'.split(
                                    '::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'userid': row['UserID'],
                    'movieid': row['MovieID'],
                    'rating': row['Rating'],
                },
                'model': 'moviedb.Rating',
                'pk': int(row['UserID'])
            }

            ratings.append(rating)

    with open('ratings.json', 'w') as f:   # place to dump/put the data
        f.write(json.dumps(ratings))
