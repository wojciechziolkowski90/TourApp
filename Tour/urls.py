from urllib import request

from django.contrib import admin
from django.urls import path, include

from Tours_app import views
from Tours_app.views import HomePageView, AboutPageView, LoginView, LogoutView, \
    TourListView, SignUp, DeleteTourView, UpdateTourView, AddTourView, ReviewView, AddReviewView, \
    ContactView, TourDetails, CategoryListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='homepage'),
    path('o-nas/', AboutPageView.as_view(), name='about'),
    path('zaloguj/', LoginView.as_view(), name='login'),
    path('wyloguj/', LogoutView.as_view(), name='logout'),
    path('rejestracja/', SignUp.as_view(), name='signup'),
    path('wycieczki/', TourListView.as_view(), name='tourlist'),
    path('usun-wycieczke/<int:pk>/', DeleteTourView.as_view(), name='tourdelete'),
    path('zaktualizuj-wycieczke/<int:pk>/', UpdateTourView.as_view(), name='tourupdate'),
    path('dodaj-wycieczke/', AddTourView.as_view(), name='addtour'),
    path('dodaj-opinie/', AddReviewView.as_view(), name='addreview'),
    path('opinie/', ReviewView.as_view(), name='review'),
    path('wycieczka/<int:pk>/', TourDetails.as_view(), name='tourdetails'),
    path('kontakt/', ContactView.as_view(), name='contact'),
    path('kategorie/<str:pk>', CategoryListView.as_view(), name='category')

]
