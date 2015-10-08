from django.shortcuts import render
from django.http import HttpResponse
from .models import Rater, Movie, Rating


def top_20_movies(request):
    movies = Movie.objects.order_by(-average_rating)[:20]
    return render(request,
                  'review/movie.html',
                  average_rating,
                  {'movies': movies})


def movie_detail(request, Movie_id):
    movies = Movie.objects.get(pk=movie_id)
    m_ratings = movie.average_rating()
    return render(request,
                'review/movie.html',
                    {'movies': movies})


def rater_detail(request, RaterID):
    raters = Rater.objects.get(RaterID)

# def Rater_info(request):
