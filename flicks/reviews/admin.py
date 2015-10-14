from django.contrib import admin
from .models import Movie, Rater, Rating

# Register your models here.
list_display = []

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']


class RaterAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'age', 'occupation', 'zipcode']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['stars']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
