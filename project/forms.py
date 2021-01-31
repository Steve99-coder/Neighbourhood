from django import forms
from .models import Neighbourhood, Profile, Post, Business


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')
