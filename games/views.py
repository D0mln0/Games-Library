from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from games.forms import GameForm, PlayerForm, PublisherSearchForm, GameSearchForm, PlayerSearchForm
from games.models import Game, Player, Publisher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "games": Game.objects.count(),
        "publishers": Publisher.objects.count(),
        "players": Player.objects.count(),
    }
    return render(request, "games/index.html", context=context)


class PublisherListView(LoginRequiredMixin, ListView):
    model = Publisher
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublisherListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = PublisherSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.model.objects.filter(name__icontains=name)
        return self.model.objects.all()


class PublisherDetailView(LoginRequiredMixin, DetailView):
    model = Publisher


class PublisherCreateView(LoginRequiredMixin, CreateView):
    model = Publisher
    fields = "__all__"
    template_name = "games/publisher_form.html"
    success_url = reverse_lazy("games:publishers-list")


class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    model = Publisher
    fields = "__all__"
    success_url = reverse_lazy("games:publishers-list")


class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    model = Publisher
    success_url = reverse_lazy("games:publishers-list")


class GameListView(LoginRequiredMixin, ListView):
    model = Game
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = GameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Game.objects.select_related("publishers")
        name = self.request.GET.get("name")
        if name:
            return self.model.objects.filter(name__icontains=name)
        return queryset


class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    queryset = Game.objects.prefetch_related("players")


class GameCreateView(LoginRequiredMixin, CreateView):
    form_class = GameForm
    template_name = "games/game_form.html"
    success_url = reverse_lazy("games:games-list")


class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = "games/game_form.html"
    success_url = reverse_lazy("games:games-list")


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy("games:games-list")


class PlayerListView(LoginRequiredMixin, ListView):
    model = Player
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = PlayerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        username = self.request.GET.get("username")
        if username:
            return self.model.objects.filter(username__icontains=username)
        return self.model.objects.all()


class PlayerDetailView(LoginRequiredMixin, DetailView):
    model = Player
    queryset = Player.objects.prefetch_related("games__publishers")


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = "games/player_form.html"
    success_url = reverse_lazy("games:players-list")


class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = "games/player_form.html"
    success_url = reverse_lazy("games:players-list")


class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = reverse_lazy("games:players-list")


@login_required
def toggle_assign_to_game(request, pk):
    player = Player.objects.get(id=request.user.id)
    if (
        Game.objects.get(id=pk) in player.games.all()
    ):  # probably could check if car exists
        player.games.remove(pk)
    else:
        player.games.add(pk)
    return HttpResponseRedirect(reverse_lazy("games:games-detail", args=[pk]))
