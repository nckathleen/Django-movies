from django.conf.urls import url
from . import views     # to see the views.py file which is in same folder

urlpatterns = [
    url(r'^movies/', views.top_20_movies),
    url(r'^movies/(?P<MovieID>)\d+)$', views.show_movie), name = 'movie_detail'),
    ]
