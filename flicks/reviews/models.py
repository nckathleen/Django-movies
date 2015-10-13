from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return "{}".format(self.id)


class Rater(models.Model):

    male = 'M'
    female = 'F'
    unknown = 'U'
    gender_choices = [(male, 'Male'), (female, 'Female'), (unknown, 'Unknown')]
    gender = models.CharField(
        max_length=1, choices=gender_choices, default=unknown)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return self.id


class Rating(models.Model):
    stars = models.PositiveSmallIntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return 'Title: {}, Rater: {}, Stars: {}'.format(self.movie, self.rater, self.rating)


# def load_ml_data():
#
#     load_movie_data()
#     load_rating_data()
#     load_rater_data()


#read movie data from ml-1m/movies.dat
def load_movie_data():
    import csv
    import json

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
            'model': 'reviews.Movie',
            'pk': int(row['MovieID'])
        }
        movies.append(movie)

    with open('movies.json', 'w') as f:  # place to dump/put the movie data
        f.write(json.dumps(movies))


# read ratings data from ml-1m/ratings.dat
def load_rating_data():
    import csv
    import json

    stars = []
    with open('ml-1m/ratings.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating'.split(
                                    '::'),
                                delimiter='\t')
    for row in reader:
        print(row)
        star = {
            'fields': {
                'movie_id': row['MovieID'],
                'rating': row['Rating'],
            },
            'model': 'reviews.Rating',
            'pk': int(row['UserID'])
        }
        stars.append(star)

    with open('ratings.json', 'w') as f:  # place to dump/put the ratings data
        f.write(json.dumps(stars))


# read rater data from ml-1m/users.dat
def load_rater_data():
    import csv
    import json
    from random import choice
    from faker import Faker

    count = 1
    fake = Faker()

    User.objects.all().delete()
    '''
from reviews.models import *
load_rater_data()
    '''

    raters = []
    with open('ml-1m/users.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split(
                                    '::'),
                                delimiter='\t')

        user_set = {fake.user_name() for _ in range(8000)}
        user_list = [x for x in user_set]
        for row in reader:
            print('Reading row: {}'.format(count))
            print(user_list[count])
            auth_user = User.objects.create_user(username=user_list[count],
                                            email=fake.email(),
                                            password='password')
            rater = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'flicks.Rater',
                'pk': auth_user.pk
            }

            raters.append(rater)
            auth_user.save()
            count += 1

    with open('raters.json', 'w') as f:  # place to dump/put the rater data
        f.write(json.dumps(raters))
