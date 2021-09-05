from django.contrib import admin
from Tours_app.models import Tour, Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_name']

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'tour_name']

