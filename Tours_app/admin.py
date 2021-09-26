from django.contrib import admin
from Tours_app.models import Tour, Region, TouristAttractions, AttractionPlan, Day, Category


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'region_name', 'region_description']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'tour_name', 'category']


@admin.register(TouristAttractions)
class TouristAttractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'attraction_name', 'attraction_type']


@admin.register(AttractionPlan)
class AttractionPlanAdmin(admin.ModelAdmin):
    list_display = ['day_id', 'tour_id', 'attraction_id']


@admin.register(Day)
class DayNameAdmin(admin.ModelAdmin):
    list_display = ['day']


@admin.register(Category)
class TourTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


