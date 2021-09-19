import pytest
from django.test import Client
from django.urls import reverse



def test_HomePageView():
    c = Client()
    response = c.get('/')
    assert response.status_code == 200


def test_AboutPageView():
    c = Client()
    response = c.get('/o-nas/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_TourListView():
    c = Client()
    response = c.get("/wycieczki/")
    tours = response.context['objects']
    assert tours.count() == 0
    assert response.status_code == 200


@pytest.mark.django_db
def test_AddTourView(tours):
    c = Client()
    url = reverse('/AddTourView/')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(tours)
    for item in tours:
        assert item in response.context['object_list']

#UpdateTourView

#DeleteTourView

#LoginView

#LogoutView

#SignUp


#AddReview
# @pytest.mark.django_db
# def test_Review(reviews):
#     c = Client()
#     url = reverse('review/')
#     response = c.get(url)
#     assert response.status_code == 200
#     assert response.context['object_list'].count() == len(reviews)
#     for review in reviews:
#         assert review in response.context['object_list']



@pytest.mark.django_db
def test_ReviewList():
    c = Client()
    response = c.get("/review/")
    reviews = response.context['reviews']
    assert reviews.count() == 0
    assert response.status_code == 200

#TourDetails
# def test_TourDetails():
#     c = Client()
#     response = c.get('tour/<int:pk>/')
#     assert response.status_code == 200

#ContactView

@pytest.mark.django_db
def test_Contact_View():
    c = Client()
    response = c.get("/contact/")
    assert response.status_code == 200

