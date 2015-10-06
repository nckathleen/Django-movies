from django.contrib import admin
from .models import Movie, Rater, Rating


# Register your models here
class MovieAdmin(admin.ModelAdmin):
    #list_display = ['title', 'rating_count']

class RaterAdmin(admin.ModelAdmin):


class RatingAdmin(admin.ModelAdmin):
#    list_display = ['rating', 'rating_count']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
