from django.shortcuts import render
from django.db.models import Avg, Count
from django.http import HttpResponse
from .models import Rater, Movie, Rating

# what the average of the stars are when we group them by movie
def top_20_movies(request):
    # movie = Movie.objects.order_by(-average_rating)[:20]
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=100)
    movies = Movie.popular_movies.annotate(Avg('rating__stars')) \
                          .order_by('-rating__stars__avg')[:20]
    return render(request,
                  'review/top_movies.html',
                  {'movies': movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
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
