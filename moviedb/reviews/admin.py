from django.contrib import admin
from reviews.models import UserProfile

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.sire.register(Rater)
