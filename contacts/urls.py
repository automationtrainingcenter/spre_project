from django.conf.urls import url
from contacts import views


urlpatterns = [
    url(r'^contact$', views.make_contact, name='make_contact'),
]
