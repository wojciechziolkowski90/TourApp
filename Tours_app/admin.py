from django.contrib import admin
from Tours_app.models import Tour, Region, Attractions, AttractionPlan, Day, Category


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']


@admin.register(Attractions)
class TouristAttractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']


@admin.register(AttractionPlan)
class AttractionPlanAdmin(admin.ModelAdmin):
    list_display = ['day', 'tour', 'attraction']


@admin.register(Day)
class DayNameAdmin(admin.ModelAdmin):
    list_display = ['day']


@admin.register(Category)
class TourTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


