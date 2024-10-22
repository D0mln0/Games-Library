from django.urls import path

from games.views import (
    index,
    PublisherListView,
    GameListView,
    PlayerListView,
    PublisherDetailView,
    GameDetailView,
    PlayerDetailView,
)

app_name = "games"

urlpatterns = [
    path("", index, name="index"),
    path("publishers/", PublisherListView.as_view(), name="publishers"),
    path("publishers/<int:pk>/", PublisherDetailView.as_view(), name="publishers-detail"),
    path("games/", GameListView.as_view(), name="games"),
    path("games/<int:pk>/", GameDetailView.as_view(), name="games-detail"),
    path("players/", PlayerListView.as_view(), name="players"),
    path("players/<int:pk>/", PlayerDetailView.as_view(), name="players-detail"),
]
