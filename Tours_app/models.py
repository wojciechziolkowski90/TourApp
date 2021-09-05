from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=100)
    passport_need = models.BooleanField(default=False)


Tour_Kind = (
    (1,"Active"),
    (2, "Culture"),
    (3, "Wine tour"),
    (4, "Trekking"),
    (5, "Incentive"),
)


class Tour(models.Model):
    tour_name = models.CharField(max_length=255)
    tour_days = models.IntegerField()
    tour_type = models.IntegerField(choices=Tour_Kind)
    tour_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour_name} {self.tour_days} {self.tour_type} {self.tour_country}"

