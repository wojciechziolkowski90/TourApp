from datetime import timezone

from django.db import models
from django.urls import reverse

Attracion_Type = [
    (1, 'Przyrodnicza'),
    (2, 'Miejska'),
    (3, 'Kulturowa'),
    (4, 'Aktywna'),
    (5, 'Winiarska'),
]
class Region(models.Model):
    region_name = models.CharField(max_length=100)
    region_description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.region_name}"

class TourType(models.Model):
    type = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('tourlist', kwargs={'pk': self.pk})

class Tour(models.Model):
    tour_name = models.CharField(max_length=255)
    tour_days = models.IntegerField()
    tour_start = models.DateField()
    tour_end = models.DateField()
    tour_attractions = models.ManyToManyField('TouristAttractions', through='AttractionPlan')
    tour_type = models.ForeignKey(TourType, on_delete=models.CASCADE)
    tour_foto = models.ImageField(upload_to='Tours_app/static/images/', blank=True)

    def __str__(self):
        return f"{self.tour_name} {self.tour_days} {self.tour_type}"

    def get_absolute_url(self):
        return reverse('tourdetails', kwargs={'pk': self.pk})


    def get_all_tour_attractions(self):
        days = DayName.objects.order_by('order')
        x = []
        for day in days:
            plans = AttractionPlan.objects.filter(day_name_id=day, tour_id=self).order_by('day_name_id')
            if plans.count() > 0:
                x.append([day.get_day_name_display(), plans])
        return x


class TouristAttractions(models.Model):
    attraction_name = models.CharField(max_length=100)
    attraction_description = models.CharField(max_length=255)
    attraction_type = models.IntegerField(choices=Attracion_Type)
    attraction_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.attraction_name} {self.attraction_description} {self.attraction_region}{self.get_attraction_type_display()}"


class DayName(models.Model):
    class DayNames(models.IntegerChoices):
        Poniedziałek = 1
        Wtorek = 2
        Środa = 3
        Czwartek = 4
        Piątek = 5
        Sobota = 6
        Niedziela = 7

    day_name = models.PositiveIntegerField(choices=DayNames.choices)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.get_day_name_display()


class AttractionPlan(models.Model):
    day_name_id = models.ForeignKey(DayName, on_delete=models.CASCADE)
    tour_id = models.ForeignKey('Tour', on_delete=models.CASCADE)
    attraction_id = models.ForeignKey(TouristAttractions, on_delete=models.CASCADE)


class Review(models.Model):
    user_name = models.CharField(max_length=100)
    user_review = models.TextField()

    def __str__(self):
        return f"{self.user_name} {self.user_review}"

