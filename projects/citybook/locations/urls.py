from django.urls import path, include
from rest_framework import routers

from .views import CountryViewSet, CityViewSet

router = routers.DefaultRouter()
router.register("country", CountryViewSet, "country")
router.register("city", CityViewSet, "city")

urlpatterns = [
    path('', include(router.urls))
]
