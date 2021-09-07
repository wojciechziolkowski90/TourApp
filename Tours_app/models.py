from django.db import models


# Create your models here.
import Tour


class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_description = models.CharField(max_length=255)
    passport_need = models.BooleanField(default=False)


# Attracion_Type = (
#     (1, 'Nature'),
#     (2, 'Urban'),
#     (3, 'Folk'),
#     (4, 'Active'),
#     (5, 'Culture'),
# )


# class TouristAttractions(models.Model):
#     region = models.CharField(max_length=100)
#     attracion_name = models.CharField(max_length=100)
#     attracion_description = models.CharField(max_length=255)
#     attracion_type = models.IntegerField(choices=Attracion_Type)
#     attration_country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     attraction_tour_plan= models.ManyToManyField(Tour)

Tour_Type = (
    (1, "Active"),
    (2, "Culture"),
    (3, "Wine tour"),
    (4, "Trekking"),
    (5, "Incentive"),
)


class Tour(models.Model):
    tour_name = models.CharField(max_length=255)
    tour_days = models.IntegerField()
    tour_type = models.IntegerField(choices=Tour_Type)
    tour_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour_name} {self.tour_days} {self.tour_type} {self.tour_country}"


class Review(models.Model):
    user_name = models.CharField(max_length=100)
    user_review = models.TextField()