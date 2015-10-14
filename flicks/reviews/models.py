from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return "{}".format(self.id)


class Rater(models.Model):

    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),)

    OCCUPATION_CHOICES = (
        (0, "other"),
        (1, "academic/educator"),
        (2, "artist"),
        (3, "clerical/admin"),
        (4, "college/grad student"),
        (5, "customer service"),
        (6, "doctor/health care"),
        (7, "executive/managerial"),
        (8, "farmer"),
        (9, "homemaker"),
        (10, "K-12 student"),
        (11, "lawyer"),
        (12, "programmer"),
        (13, "retired"),
        (14, "sales/marketing"),
        (15, "scientist"),
        (16, "self-employed"),
        (17, "technician/engineer"),
        (18, "tradesman/craftsman"),
        (19, "unemployed"),
        (20, "writer"))

    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.IntegerField(choices=OCCUPATION_CHOICES)
    zipcode = models.CharField(max_length=10)
    user = models.OneToOneField(User, primary_key=True)

    def __str__(self):
        return str(self.user)


class Rating(models.Model):
    stars = models.PositiveSmallIntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return 'Title: {}, Rater: {}, Stars: {}'.format(self.movie, self.rater, self.stars)


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
        star = {
            'fields': {
                'movie_id': row['MovieID'],
                'rater_id': row['UserID'],
                'stars': row['Rating'],
            },
            'model': 'reviews.Rating'
        }
        stars.append(star)

    with open('ratings.json', 'w') as f:  # place to dump/put the ratings data
        f.write(json.dumps(stars))


# read rater data from ml-1m/users.dat
def load_rater_data():
    import csv
    import json
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
            auth_user = User(username=user_list[count],
                                            email=fake.email(),
                                            password='password',
                                            pk=row['UserID'])
            rater = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'reviews.Rater',
                'pk': auth_user.pk
            }
            raters.append(rater)
            auth_user.save()
            count += 1

    with open('raters.json', 'w') as f:  # place to dump/put the rater data
        f.write(json.dumps(raters))
