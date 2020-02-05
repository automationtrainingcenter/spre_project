from django.shortcuts import render, redirect
from accounts.views import dashboard

# Create your views here.


def make_contact(request):

    return redirect(dashboard)
