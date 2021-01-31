from django import forms
from .models import Neighbourhood, Profile, Post, Business


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)
