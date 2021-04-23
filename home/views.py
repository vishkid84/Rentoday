from django.shortcuts import render
from listings.models import Listing
from listings.views import listings

from django.shortcuts import render, get_object_or_404, redirect, reverse

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-date')[0:3]

    context = {
        'listings': listings,
    }
    return render(request, 'home/index.html', context)
