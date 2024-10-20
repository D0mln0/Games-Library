from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255)


class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    publishers = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )
    players = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )


class Player(AbstractUser):
    pass
