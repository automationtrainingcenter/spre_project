from django.shortcuts import render
from listings.models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import bedroom_choices, price_choices, state_choices

# Create your views here.


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listings = paginator.page(paginator.num_pages)

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
    listings = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            listings = listings.filter(state=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    # paginator

    context = {
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'listings': listings
    }
    return render(request, 'listings/search.html', context)
