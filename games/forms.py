from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from games.models import Game, Player


class GameForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Game
        fields = "__all__"


class PlayerForm(UserCreationForm):
    class Meta:
        model = Player
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )


class PlayerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        ),
    )


class GameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by game name"}
        )
    )


class PublisherSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by publisher name"}
        )
    )
