from django.urls import path

from games.views import (
    index,
    PublisherListView,
    PublisherDetailView,
    PublisherCreateView,
    PublisherUpdateView,
    PublisherDeleteView,
    GameListView,
    GameDetailView,
    GameCreateView,
    GameUpdateView,
    GameDeleteView,
    PlayerListView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView,
)

app_name = "games"

urlpatterns = [
    path("", index, name="index"),
    path("publishers/", PublisherListView.as_view(), name="publishers-list"),
    path("publishers/<int:pk>/", PublisherDetailView.as_view(), name="publishers-detail"),
    path("publishers/create/", PublisherCreateView.as_view(), name="publishers-create"),
    path("publishers/update/<int:pk>/", PublisherUpdateView.as_view(), name="publishers-update"),
    path("publishers/delete/<int:pk>/", PublisherDeleteView.as_view(), name="publishers-delete"),

    path("games/", GameListView.as_view(), name="games-list"),
    path("games/<int:pk>/", GameDetailView.as_view(), name="games-detail"),
    path("games/create/", GameCreateView.as_view(), name="games-create"),
    path("games/update/<int:pk>/", GameUpdateView.as_view(), name="games-update"),
    path("games/delete/<int:pk>/", GameDeleteView.as_view(), name="games-delete"),

    path("players/", PlayerListView.as_view(), name="players-list"),
    path("players/<int:pk>/", PlayerDetailView.as_view(), name="players-detail"),
    path("players/create/", PlayerCreateView.as_view(), name="players-create"),
    path("players/update/<int:pk>/", PlayerUpdateView.as_view(), name="players-update"),
    path("players/delete/<int:pk>/", PlayerDeleteView.as_view(), name="players-delete"),
]
