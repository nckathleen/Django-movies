from django.shortcuts import render
from django.http import HttpResponse
from .models import Rater, Movie, Rating


def top_20_movies(request):
    movie = Movie.objects.order_by(-average_rating)[:20]
    return render(request,
                  'review/movie.html',
                  {'movie': movie})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request
                  'reviews/movie_detail.html',
                  {'movie': movie})


def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    movie_ratings = []
    for rating in rater.rating_set.all():
        movie_ratings.append({
            'movie':rating.movie,
            'ratings': '\u2605' * rating.ratings
        })
    return render (request,
                   'review/rater_detail.html',
                   {'rater':rater,
                   'movie_ratings': movie_ratings})
