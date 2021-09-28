import pytest

from Tours_app.models import Tour, Review, Category, UserReservation


@pytest.fixture
def category():
    x = Category(type='a', slug='b')
    x.save()
    return x


@pytest.fixture
def tours(category):
       a = Tour.objects.create(
            tour_name='kavkaz',
            tour_days=1,
            tour_start='2021-9-21',
            tour_end='2021-9-26',
            tour_price=5000,
            category=category,
        )



@pytest.fixture
def reviews():
    lst = []
    for i in range(10):
        a = Review.objects.create(user_name=i,
                                  user_review=i)
        lst.append(a)
    return lst


@pytest.fixture
def reservation(tours):
    res = []
    for r in range(5):
        x = UserReservation.objects.create(name='wojtek', surname='ziolkow', e_mail='w@wp.pl', wycieczka=tours)
        res.append(x)
    return res


