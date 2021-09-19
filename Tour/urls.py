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
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('wycieczki/', TourListView.as_view(), name='tourlist'),
    path('DeleteTourView/<int:pk>/', DeleteTourView.as_view(), name='tourdelete'),
    path('UpdateTourView/<int:pk>/', UpdateTourView.as_view(), name='tourupdate'),
    path('AddTourView/', AddTourView.as_view(), name='addtour'),
    path('Addreview/', AddReviewView.as_view(), name='addreview'),
    path('review/', ReviewView.as_view(), name='review'),
    path('tour/<int:pk>/', TourDetails.as_view(), name='tourdetails'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('kategorie/<str:pk>', CategoryListView.as_view(), name='category')

]
