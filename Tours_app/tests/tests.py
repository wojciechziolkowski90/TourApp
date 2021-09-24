import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse, resolve
from Tours_app.models import Tour



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
@pytest.mark.django_db
def test_TourListView():
    c = Client()
    response = c.get("/wycieczki/")
    tours = response.context['objects']
    assert tours.count() == 0
    assert response.status_code == 200


#CategoryListView



# Add tour view
@pytest.mark.django_db
def test_AddTour(tours):
    c = Client()
    url = reverse('tourlist')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['objects'].count() == len(tours)
    for a in tours:
        assert a in response.context['objects']


# UpdateTourView
@pytest.mark.django_db
def test_Update(tours):
    c = Client()
    url = reverse('tourlist')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['objects'].count() == len(tours)
    for a in tours:
        assert a in response.context['objects']



# DeleteTourView
@pytest.mark.django_db
def test_DeleteTourView(tours):
    c = Client()
    url = reverse('tourlist')
    response = c.get(url)
    assert response.status_code == 200



# LoginView
@pytest.mark.django_db
def test_LoginView():
    c = Client()
    response = c.get('/zaloguj/', {'username': 'w', 'password': 'panwojtas'})
    assert response.status_code == 200
    response = c.post('login')
    response.content


# LogoutView
@pytest.mark.django_db
def test_LogoutView():
    c = Client()
    response = c.get('/')
    assert response.status_code == 200


# SignUp
@pytest.mark.django_db
def test_SignUp():
    User.objects.create_user('john', 'johnpassword')
    assert User.objects.count() == 1


# AddReview
@pytest.mark.django_db
def test_AddReview(reviews):
    c = Client()
    url = reverse('review')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['reviews'].count() == len(reviews)
    for review in reviews:
        assert review in response.context['reviews']


# ReviewList
@pytest.mark.django_db
def test_ReviewList():
    c = Client()
    response = c.get("/opinie/")
    reviews = response.context['reviews']
    assert reviews.count() == 0
    assert response.status_code == 200


# TourDetails
@pytest.mark.django_db
def test_TourDetails(tours):
    c = Client()
    url = reverse('tourlist')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['objects'].count() == len(tours)
    for a in tours:
        assert a in response.context['objects']



# ContactView
@pytest.mark.django_db
def test_Contact_View():
    c = Client()
    response = c.get("/kontakt/")
    assert response.status_code == 200


