import datetime

import pytest, http

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse, resolve
from Tours_app.models import Category, Tour


# HomePageView
def test_HomePageView():
    c = Client()
    response = c.get('/')
    assert response.status_code == 200


# AboutView
def test_AboutPageView():
    c = Client()
    response = c.get('/o-nas/')
    assert response.status_code == 200


# Add tour view
@pytest.mark.django_db
def test_addtour(client):
    category = Category.objects.create(type="wine", slug="wine")

    response = client.post(
        reverse("addtour"),
        data={
            "tour_name": "offroad",
            "tour_days": 3,
            "tour_start": "2021-01-01",
            "tour_end": "2021-01-04",
            "tour_price": 99,
            "category": category.id,
        },
    )

    assert response.status_code == http.HTTPStatus.FOUND
    assert Tour.objects.count() == 1
    assert Tour.objects.last().tour_name == "offroad"
    assert Tour.objects.last().tour_days == 3
    assert Tour.objects.last().tour_start == datetime.date(2021, 1, 1)
    assert Tour.objects.last().tour_end == datetime.date(2021, 1, 4)
    assert Tour.objects.last().tour_price == 99


# TourListView
@pytest.mark.django_db
def test_tourlist(client):
    category = Category.objects.create(type="trek", slug="hike")
    for i in range(5):
        Tour.objects.create(
            tour_name=f"kavkaz{i}",
            tour_days=1,
            tour_start="2021-01-01",
            tour_end="2021-01-02",
            tour_price=999,
            category=category,
        )

    response = client.get(
        reverse("tourlist"),
    )

    assert response.status_code == http.HTTPStatus.OK
    for i in range(5):
        assert f"kavkaz{i}" in response.content.decode()

# UpdateTourView


# DeleteTourView


# LoginView


# LogoutView


# SignUp


# AddReview


# ReviewList


# TourDetails


# ContactView


# Add Reservation


# ReservationListView
