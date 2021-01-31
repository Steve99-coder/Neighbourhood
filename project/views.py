from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import BusinessForm, PostForm, NeighbourHoodForm
from .models import Neighbourhood,Business,Post
from users.models import Profile

# Create your views here.
