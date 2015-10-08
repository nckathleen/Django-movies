from django.shortcuts import render
from django.http import HttpResponse
from .models import Rater, Movie, Rating


def top_20_movies(request):
    movies = Movie.objects.order_by(-average_rating)[:20]
    return render(request,
                  'review/movie.html',
                  {'movies': movies})


def movie_info(request, MovieID):
    movies = Movie.objects.get(MovieID)
    m_ratings = movie.average_rating()


#
# def Rater_info(request):
