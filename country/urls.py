
from django.urls import path
from . import views
urlpatterns = [
   path("",views.country,name="countrypage"),
   path('addcountry/',views.countryDetails,name="countrydetails"),
   path('postdetails/',views.postDetails,name='postdetails')
]