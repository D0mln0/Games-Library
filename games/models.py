from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    publishers = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )
    players = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="games"
    )

    def __str__(self):
        return f"{self.publishers}: {self.name}"


class Player(AbstractUser):

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("games:players-detail", kwargs={"pk": self.pk})
