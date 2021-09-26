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


class Category(models.Model):
    type = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('tourlist', kwargs={'pk': self.pk})


class Tour(models.Model):
    tour_name = models.CharField('Nazwa wycieczki', max_length=255)
    tour_days = models.IntegerField('Ilość dni')
    tour_start = models.DateField('Wyjazd')
    tour_end = models.DateField('Powrót')
    tour_price = models.IntegerField('Cena')
    tour_attractions = models.ManyToManyField('TouristAttractions', through='AttractionPlan')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='types')

    def __str__(self):
        return f"{self.tour_name}"

    def get_absolute_url(self):
        return reverse('tourdetails', kwargs={'pk': self.pk})

    def get_all_tour_attractions(self):
        days = Day.objects.order_by('order')
        x = []
        for day in days:
            plans = AttractionPlan.objects.filter(day_id=day, tour_id=self).order_by('day_id')
            if plans.count() > 0:
                x.append([day.get_day_display(), plans])
        return x


class TouristAttractions(models.Model):
    attraction_name = models.CharField(max_length=100)
    attraction_description = models.CharField(max_length=255)
    attraction_type = models.IntegerField(choices=Attracion_Type)
    attraction_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.attraction_name} {self.attraction_description} {self.attraction_region}{self.get_attraction_type_display()}"


class Day(models.Model):
    class Day(models.Choices):
        Dzień_1 = 1
        Dzień_2 = 2
        Dzień_3 = 3
        Dzień_4 = 4
        Dzień_5 = 5
        Dzień_6 = 6
        Dzień_7 = 7
        Dzień_8 = 8
        Dzień_9 = 9
        Dzień_10 = 10



    day = models.PositiveIntegerField(choices=Day.choices)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.get_day_display()


class AttractionPlan(models.Model):
    day_id = models.ForeignKey(Day, on_delete=models.CASCADE)
    tour_id = models.ForeignKey('Tour', on_delete=models.CASCADE)
    attraction_id = models.ForeignKey(TouristAttractions, on_delete=models.CASCADE, null=True)


class Review(models.Model):
    user_name = models.CharField('Imię', max_length=100)
    user_review = models.TextField('Opinia')

    def __str__(self):
        return f"{self.user_name} {self.user_review}"


class UserReservation(models.Model):
    name = models.CharField('Imię', max_length=100)
    surname = models.CharField('Nazwisko', max_length=100)
    e_mail = models.EmailField()
    wycieczka= models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.e_mail}"
