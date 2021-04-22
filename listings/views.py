from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .models import Listing
from .forms import ListingForm
from django.contrib.auth.models import User

# Create your views here.


def listings(request):
    listings = Listing.objects.all().order_by('-date')
    latest = Listing.objects.order_by('-date')[0:3]
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


@login_required
def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            listing = form.save()
            messages.success(request, 'Successfully added new listing')
            return redirect(reverse('listing_detail', args=[listing.id]))
        else:
            messages.error(
                request, 'Failed to add new. Please ensure the form is valid.')
    else:
        form = ListingForm()

    template = 'listings/add_listing.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.user != listing.user:
        messages.error(
            request, 'Sorry, you dont have the permission to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        if request.user == listing.user:
            form = ListingForm(request.POST, request.FILES, instance=listing)
            if form.is_valid:
                form.instance.user = request.user
                form.save()
                messages.success(request, 'Successfully updated the listing')
                return redirect(reverse('listing_detail', args=[listing.id]))
            else:
                messages.error(
                    request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = ListingForm(instance=listing)

    template = 'listings/edit_listing.html'
    context = {
        'listing': listing,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_listing(request, listing_id):
    ''' Logged in user can delete their comment if any'''
    listing = get_object_or_404(Listing, pk=listing_id)
    listing.delete()
    messages.success(request, 'Listing deleted')
    return redirect(reverse('listings'))
