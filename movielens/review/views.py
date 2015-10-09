from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg, Count
from .models import Rater, Movie


def top_20_movies(request):

    popular_movies = Movie.objects.annotate(num_ratings=Count('rating'))\
        .filter(num_ratings__gte=50)

    movies = popular_movies.annotate(
        Avg('rating__ratings')).order_by('-rating__ratings__avg')[:20]

    return render(request,
                  'review/top_20_movies.html',
                  average_rating,
                  {'movies': movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    m_ratings = movie.average_rating()
    return render(request,
                  'review/top_movies.html',
                  {'movie': movie})


def rater_detail(request, rater_id):
    raters = Rater.objects.get(pk=rater_id)
    movie_ratings = []
    for rating in rater.rating_set.all():
        movie_ratings.append({
            'movie': rating.movie,
            'ratings': '\u2605' * rating.ratings})

    return render(request,
                  'review/rater_detail.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})
