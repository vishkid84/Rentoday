from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Listing
from .forms import ListingForm

# Create your views here.


def listings(request):
    listings = Listing.objects.all().order_by('-date')
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(listing_name__icontains=query) | Q(
                description__icontains=query)
            listings = listings.filter(queries)

    template = 'listings/listings.html'
    context = {
        'listings': listings,
        'search_term': query,
    }

    return render(request, template, context)


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    template = 'listings/listing_detail.html'
    context = {
        'listing': listing,
    }

    return render(request, template, context)


def add_listing(request):
    form = ListingForm(request.POST or None)

    template = 'listings/add_listing.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
