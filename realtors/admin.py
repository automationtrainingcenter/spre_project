from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_num', 'is_mvp')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    search_fields = ('name', 'phone_num')


admin.site.register(Realtor, RealtorAdmin)
