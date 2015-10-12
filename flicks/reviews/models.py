from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating():
        return

    def __str__(self):
        return "{} {}".format(self.id, self.title)


class Rater(models.Model):

    male = 'M'
    female = 'F'
    unknown = 'U'
    gender_choices = [(male, 'Male'), (female, 'Female'), (unknown, 'Unknown')]
    gender = models.CharField(
        max_length=1, choices=gender_choices, default=unknown)
    user = models.OneToOneField(User, primary_key=True)

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
    from faker import Faker

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
                'rating': row['Rating'],
            },
            'model': 'flicks.Rating',
            'pk': int(row['UserID'])
        }

        stars.append(star)

    with open('ratings.json', 'w') as f:  # place to dump/put the ratings data
        f.write(json.dumps(stars))


# read rater data from ml-1m/users.dat
def load_rater_data():
    import csv
    import json

    raters = []
    with open('ml-1m/users.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split(
                                    '::'),
                                delimiter='\t')

    for row in reader:
        auth_user = User.objects.create_user(username=fake.user_name,
                                            email=fake.email,
                                            password=make_password('password'),
                                            first_name=fake.first_name(),
                                            last_name=fake.last_name())
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

    with open('raters.json', 'w') as f:  # place to dump/put the rater data
        f.write(json.dumps(raters))
