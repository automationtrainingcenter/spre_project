from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'price', 'is_published', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'city', 'state')
    list_filter = ('realtor', 'list_date', 'city', 'state')


admin.site.register(Listing, ListingAdmin)
