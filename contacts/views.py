from django.shortcuts import render, redirect
from accounts.views import dashboard
from contacts.models import contact
from django.contrib import messages


# Create your views here.


def make_contact(request):
    if request.user.is_authenticated():
        user_id = request.user.id
    else:
        user_id = 0

    listing = request.GET.get('listing')
    listing_id = request.GET.get('listing_id')
    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    message = request.GET.get('message')

    if request.user.is_authenticated():
        cts = contact.objects.filter(listing_id=listing_id, user_id=user_id)
        if cts:
            messages.error(
                request, "You already sent an Inquiry about this Property")
            return redirect('/listings/'+listing_id)

    ctct = contact(user_id=user_id, listing=listing, listing_id=listing_id,
                   name=name, email=email, phone=phone, message=message)
    ctct.save()

    messages.success(
        request, 'Your Inquiry submitted. We will get back you soon')

    return redirect('/listings/'+listing_id)
