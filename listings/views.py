from django.shortcuts import render
from listings.models import Listing

# Create your views here.


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
