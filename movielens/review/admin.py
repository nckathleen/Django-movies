from django.contrib import admin
from .models import Movie, Rater, Rating


# Register your models here
class MovieAdmin(admin.ModelAdmin):
    pass
    #list_display = ['title', 'rating_count']


class RaterAdmin(admin.ModelAdmin):
    pass

class RatingAdmin(admin.ModelAdmin):
    pass
#    list_display = ['rating', 'rating_count']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
