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


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    template = 'listings/listing_detail.html'
    context = {
        'listing': listing,
    }

    return render(request, template, context)
