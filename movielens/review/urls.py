from django.conf.urls import url
from . import views     # to see the views.py file which is in same folder

urlpatterns = [
    url(r'^movies/', views.top_20_movies),
    url(r'^movies/(?P<movie_id>\d+)', views.movie_detail, name='movie_detail')]
