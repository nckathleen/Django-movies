from django.core.management.base import BaseCommand
from updates.models import Favorite, Status
from profiles.models import Profile
from django.contrib.auth.models import User
from faker import Faker
from django.db.utils import IntegrityError
import random

# This is borrowed code.  Not movielens-specific!!  

class Command(BaseCommand):
    def handle(self, *args, **options):
        '''Create some fake users and statuses'''
        fake = Faker()

        Favorite.objects.all().delete()
        Status.objects.all().delete()
        User.objects.exclude(username='admin').delete()

        users = []
        statuses = []

        for _ in range(50):
            new_user = User(username=fake.user_name(),
                            email=fake.email())
            new_user.set_password('password')
            new_user.save()
            profile = Profile(user=new_user, favorite_color='blue')
            profile.save()
            users.append(new_user)

        for _ in range(1000):
            new_status = Status(user=random.choice(users),
                                posted_at=fake.date_time_this_year(),
                                text=fake.text(max_nb_chars=141))
            new_status.save()
            statuses.append(new_status)

        for _ in range(4000):
            try:
                favorite = Favorite(user=random.choice(users),
                                    status=random.choice(statuses))
                favorite.save()
            except IntegrityError:
                continue
