from django.db import models
from django.contrib.auth.models import User
from faker import Faker

# Create your models here.
class Profile(models.model):
    user = models.OneToOneField(User, primary_key=True, null=True)
    last_name = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    email = models.CharField(max_length=60)
    password = 'password'
