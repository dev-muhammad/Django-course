from django.urls import path, include
from rest_framework import routers

from .views import PlaceViewSet

router = routers.DefaultRouter()
router.register("place", PlaceViewSet, "place")

urlpatterns = [
    path('', include(router.urls))
]
