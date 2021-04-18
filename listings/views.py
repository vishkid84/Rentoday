from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import Listing

# Create your views here.


def listings(request):
    listings = Listing.objects.all().order_by('-date')

    template = 'listings/listings.html'
    context = {
        'listings': listings,
    }

    return render(request, template, context)
