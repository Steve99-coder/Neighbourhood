from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import BusinessForm, PostForm, NeighbourHoodForm
from .models import Neighbourhood,Business,Post
from users.models import Profile

# Create your views here.
def index(request):
    return render(request, 'neighbourhood/index.html')


def neighbourhoods(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'neighbourhood/neighbourhoods.html', params)
