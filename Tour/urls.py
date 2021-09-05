
from django.contrib import admin
from django.urls import path

from Tours_app.views import HomePageView, GruzjaView, KirgistanView, WietnamView, AboutPageView, LoginView, LogoutView, \
    TourListView, TourDetails, SignUp

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
    path('szczegoly/', TourDetails.as_view(), name='tourdetails'),
]
