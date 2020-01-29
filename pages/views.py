from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, price_choices, bedroom_choices


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/home.html', context)


def about(request):
    realtors = Realtor.objects.order_by('hire_date')[:3]
    sop_realtor = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'sop_realtor': sop_realtor
    }
    return render(request, 'pages/about.html', context)
