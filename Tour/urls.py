
from django.contrib import admin
from django.urls import path, include

from Tours_app.views import HomePageView, GruzjaView, KirgistanView, WietnamView, AboutPageView, LoginView, LogoutView, \
    TourListView, SignUp, TourDetailsView, DeleteTourView, UpdateTourView, AddTourView, ReviewView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='homepage'),
    path('gruzja/', GruzjaView.as_view(), name='gruzja'),
    path('kirgistan/', KirgistanView.as_view(), name='kirgistan'),
    path('wietnam/', WietnamView.as_view(), name='wietnam'),
    path('o-nas/', AboutPageView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('wycieczki/', TourListView.as_view(), name='tourlist'),
    path('TourDetailsView/<int:pk>/', TourDetailsView.as_view(), name='tourdetails'),
    path('DeleteTourView/<int:pk>/', DeleteTourView.as_view(), name='tourdelete'),
    path('UpdateTourView/<int:pk>/', UpdateTourView.as_view(), name='tourupdate'),
    path('AddTourView/', AddTourView.as_view(), name='addtour'),
    path('review/', ReviewView.as_view(), name='review')
]
