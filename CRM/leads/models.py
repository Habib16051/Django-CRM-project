from django.db import models

# Django Default User Model
# from django.contrib.auth import get_user_model
# User = get_user_model()

# Django Custom User Model for production Level Use

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


# Create your models here.


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
