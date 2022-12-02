from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone_number', 'country_code', 'is_favorite')
    list_filter = ('firstname', 'lastname', 'phone_number', 'country_code', 'is_favorite')
    search_fields = ('firstname', 'lastname', 'phone_number', 'country_code', 'is_favorite')
