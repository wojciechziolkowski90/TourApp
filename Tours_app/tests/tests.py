import datetime
from unittest.mock import patch

import pytest, http
from django.conf import settings
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse, resolve
from Tours_app.models import Category, Tour, Review, AttractionPlan, Day, TouristAttractions, Region, UserReservation


# HomePageView
def test_HomePageView(client):
    response = client.get('/')
    assert response.status_code == 200


# AboutView
def test_AboutPageView(client):
    response = client.get('/o-nas/')
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


# CategoryView
@pytest.mark.django_db
def test_category(client):
    category = Category.objects.create(type="Foto", slug="foto")
    tour = Tour.objects.create(
        tour_name="Kachetia",
        tour_days=5,
        tour_start="2021-01-01",
        tour_end="2021-01-06",
        tour_price=9999,
        category=category,
    )
    response = client.get(
        reverse("category"), args=[tour.id])

    assert response.status_code == http.HTTPStatus.OK


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
@pytest.mark.django_db
def test_updateview(client):
    category = Category.objects.create(type="culture", slug="trip")
    tour = Tour.objects.create(
        tour_name="gruzja",
        tour_days=4,
        tour_start="2021-01-01",
        tour_end="2021-01-05",
        tour_price=3500,
        category=category,
    )

    response = client.post(
        reverse("tourupdate", args=[tour.id]),
        data={
            "tour_name": "georgia",
            "tour_days": 9,
            "tour_start": "2021-01-01",
            "tour_end": "2021-01-10",
            "tour_price": 5000,
            "category": category.id,
        },
    )

    assert response.status_code == http.HTTPStatus.FOUND
    assert Tour.objects.get(id=tour.id).tour_name == "georgia"
    assert Tour.objects.get(id=tour.id).tour_days == 9
    assert Tour.objects.get(id=tour.id).tour_start == datetime.date(2021, 1, 1)
    assert Tour.objects.get(id=tour.id).tour_end == datetime.date(2021, 1, 10)
    assert Tour.objects.get(id=tour.id).tour_price == 5000


# DeleteTourView
@pytest.mark.django_db
def test_deleteview(client):
    category = Category.objects.create(type="narty", slug="narty")
    tour = Tour.objects.create(
        tour_name="Narty",
        tour_days=7,
        tour_start="2021-01-01",
        tour_end="2021-01-08",
        tour_price=4999,
        category=category,
    )

    response = client.post(
        reverse("tourdelete", args=[tour.id]),
    )

    assert response.status_code == http.HTTPStatus.FOUND
    assert not Tour.objects.filter(id=tour.id).exists()


# SignUp
User = get_user_model()


@pytest.mark.django_db
def test_signup(client):
    response = client.post(
        reverse("signup"),
        data={
            "username": "wojtek",
            "password": "wojtek3000",
            "re_password": "wojtek3000",
        },
    )

    assert response.status_code == http.HTTPStatus.FOUND
    assert User.objects.filter(username="wojtek").exists()


@pytest.mark.django_db
def test_failed_signup(client):
    response = client.post(
        reverse("signup"),
        data={
            "username": "wojtek",
            "password": "wojtek2000",
            "re_password": "wojtek4000",
        },
    )

    assert response.status_code == http.HTTPStatus.OK
    assert not User.objects.filter(username="wojtek").exists()


# LoginView

@pytest.mark.django_db
def test_login(client):
    user = User.objects.create_user(username="wojt", password="wojtek5000")
    response = client.post(
        reverse("login"),
        data={
            "username": "wojt",
            "password": "wojtek5000",
        },
    )
    assert response.status_code == http.HTTPStatus.FOUND
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_failed_login(client):
    user = User.objects.create_user(username="kasia", password="kasia6000")
    response = client.post(
        reverse("login"),
        data={
            "username": "kasia",
            "password": "kasia7000",
        },
    )

    assert response.status_code == http.HTTPStatus.OK
    assert Tour.objects.count() == 0


# LogoutView
@pytest.mark.django_db
def test_logout(client):
    user = User.objects.create_user(username="wojtek", password="wojtek8000")
    client.force_login(user)

    response = client.get(
        reverse("logout"),
    )

    assert response.status_code == http.HTTPStatus.FOUND
    assert not client.session.get("_auth_user_id")


# AddReview
@pytest.mark.django_db
def test_addreview(client):
    response = client.post(
        reverse("addreview"),
        data={
            "user_name": "Wojtek",
            "user_review": "Ekstra",
        },
    )

    assert response.status_code == http.HTTPStatus.FOUND
    assert Review.objects.count() == 1
    assert Review.objects.last().user_name == "Wojtek"
    assert Review.objects.last().user_review == "Ekstra"


# ReviewList
@pytest.mark.django_db
def test_reviewlist(client):
    for i in range(5):
        Review.objects.create(
            user_name=f"Wojtek{i}",
            user_review="Ekstra",
        )

    response = client.get(
        reverse("review"),
    )

    assert response.status_code == http.HTTPStatus.OK
    for i in range(5):
        assert f"Wojtek{i}" in response.content.decode()


# TourDetails
@pytest.mark.django_db
def test_detailsview(client):
    category = Category.objects.create(type="narty", slug="narty")
    tour = Tour.objects.create(
        tour_name="Narty",
        tour_days=7,
        tour_start="2021-01-01",
        tour_end="2021-01-08",
        tour_price=4999,
        category=category,
    )

    response = client.post(
        reverse("tourdetails", args=[tour.id]),
    )

    assert Tour.objects.filter(id=tour.id).exists()
    assert Tour.objects.last().tour_name == "Narty"


# ContactView
@patch("Tours_app.views.send_mail")
@pytest.mark.django_db
def test_mail(test_send_mail, client):
    test_send_mail.return_value = None
    response = client.post(
        reverse("contact"),
        data={
            "odbiorca": "w@wp.pl",
            "imie": "Wojtek",
            "tekst": "siema",
        },
    )

    assert response.status_code == http.HTTPStatus.OK
    test_send_mail.assert_called_with(
        "Kontakt z adventuretours",
        "Wojtek",
        settings.DEFAULT_FROM_EMAIL,
        ["w@wp.pl"],
    )


# Add Reservation
@pytest.mark.django_db
def test_addreservation(client):
    category = Category.objects.create(type="Offroad", slug="wine")
    tour = Tour.objects.create(
        tour_name="Offroad",
        tour_days=7,
        tour_start="2021-01-01",
        tour_end="2021-01-08",
        tour_price=4999,
        category=category,
    )
    response = client.post(
        reverse("reservation"),
        data={
            "name": "Wojtek",
            "surname": "Ziolkowski",
            "e_mail": "wp@wp.pl",
            "wycieczka": tour.id
        },
    )

    assert response.status_code == http.HTTPStatus.FOUND
    assert UserReservation.objects.count() == 1
    assert UserReservation.objects.last().name == "Wojtek"
    assert UserReservation.objects.last().surname == "Ziolkowski"


# ReservationListView
@pytest.mark.django_db
def test_reservationlist(client):
    category = Category.objects.create(type="Offroad", slug="wine")
    tour = Tour.objects.create(
        tour_name="Offroad",
        tour_days=7,
        tour_start="2021-01-01",
        tour_end="2021-01-08",
        tour_price=4999,
        category=category,
    )
    for i in range(5):
        UserReservation.objects.create(
            name="Wojtek",
            surname="Ziolkowski",
            e_mail="wp@wp.pl",
            wycieczka=tour
        )

        response = client.get(
            reverse("reservationlist"),
        )

        assert response.status_code == http.HTTPStatus.OK
        for i in range(5):
            assert "Wojtek" in response.content.decode()
            assert "Ziolkowski" in response.content.decode()
