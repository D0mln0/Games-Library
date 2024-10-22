from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from games.models import Game, Player,Publisher


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "games": Game.objects.count(),
        "publishers": Publisher.objects.count(),
        "players": Player.objects.count(),
    }
    return render(request, "games/index.html", context=context)
