from datetime import datetime, date

import pytest

from Tours_app.models import Tour, Review, Category


@pytest.fixture
def tourType():
    x = Category(type='a', slug='b')
    x.save()
    return x


@pytest.fixture
def tours(tourType):
    lst = []
    for i in range(2):
        a = Tour.objects.create(
            tour_name='kavkaz',
            tour_days=1,
            tour_start='2021-9-21',
            tour_end='2021-9-26',
            tour_type=tourType,
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
