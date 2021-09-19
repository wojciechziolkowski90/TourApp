import pytest

from Tours_app.models import Tour, Review


@pytest.fixture
def tours():
    lst = []
    for i in range(10):
        a = Tour.objects.create(tour_name=i,
                                tour_days=i
                                )
        lst.append(a)
    return lst


@pytest.fixture
def reviews():
    lst = []
    for i in range(10):
        a = Review.objects.create(user_name=i,
                                user_review=i)
        lst.append(a)
    return lst
