from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from games.models import Game, Player, Publisher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def index(request: HttpRequest) -> HttpResponse:
    context = {
        "games": Game.objects.count(),
        "publishers": Publisher.objects.count(),
        "players": Player.objects.count(),
    }
    return render(request, "games/index.html", context=context)


class PublisherListView(LoginRequiredMixin, ListView):
    model = Publisher
    paginate_by = 10


class PublisherDetailView(LoginRequiredMixin, DetailView):
    model = Publisher


class GameListView(LoginRequiredMixin, ListView):
    model = Game
    paginate_by = 10


class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    queryset = Game.objects.prefetch_related("players")


class PlayerListView(LoginRequiredMixin, ListView):
    model = Player
    paginate_by = 10


class PlayerDetailView(LoginRequiredMixin, DetailView):
    model = Player
