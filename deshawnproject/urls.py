from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from deshawnapi.views import WalkerView, CityView, DogView, AppointmentView


# API only supports requests to /walkers, /cities, /dogs any other will get 404
# first argument is what url path is
# second is view that will handle client requests to that route
# third is needed in order for route to be registered, but unused in our API here
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'walkers', WalkerView, 'walk')
router.register(r'cities', CityView, 'city')
router.register(r'dogs', DogView, 'dog')
router.register(r'appointments', AppointmentView, 'appointment')

urlpatterns = [
    path('', include(router.urls)),
]

