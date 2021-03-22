from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'listing', 'email')
    list_display_links = ('name', 'id', )
    search_fields = ('name', 'email', 'listing', 'id')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
