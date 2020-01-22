from django.conf.urls import url
from listings import views


urlpatterns = [
    url(r'^$', views.listings, name='listings'),
    url(r'(?P<listing_id>\d+)/$', views.listing, name='listing'),
    url(r'search/$', views.search, name='search')

]
