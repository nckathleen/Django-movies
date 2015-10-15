from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db.models import Avg, Count
from django.http import HttpResponse
from .models import Rater, Movie, Rating
from .forms import UserForm


def user_login(request):
    if request.method == "POST":    # attempting to log in
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('movie_detail')
        else:
            return render(request,
                          'user/login.html',
                          {'failed': True,
                          'username':username})

    return render(request,
                  'reviews/login.html')


def user_register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            return redirect('all_statuses')
    else:
        form = UserForm()
    return render(request, 'reviews/register.html',
                  {'form': form})


# what the average of the stars are when we group them by movie
def top_20_movies(request):
    # movie = Movie.objects.order_by(-average_rating)[:20]
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=100)
    movies = Movie.popular_movies.annotate(Avg('rating__stars')) \
                          .order_by('-rating__stars__avg')[:20]
    return render(request,
                  'reviews/top_movies.html',
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
            'ratings': '\u2605' * rating.stars
        })
    return render (request,
                   'reviews/rater_detail.html',
                   {'rater':rater,
                   'movie_ratings': movie_ratings})
