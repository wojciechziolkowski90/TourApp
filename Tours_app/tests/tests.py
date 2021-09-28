import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse, resolve



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


# TourListView



# Add tour view



# UpdateTourView


# DeleteTourView



# LoginView


# LogoutView


# SignUp


# AddReview


# ReviewList


# TourDetails


# ContactView


#Add Reservation


#ReservationListView



