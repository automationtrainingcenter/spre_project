from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard')
]
