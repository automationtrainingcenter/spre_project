from django.contrib import admin
from contacts.models import contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'listing_id', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone')


admin.site.register(contact, ContactAdmin)
