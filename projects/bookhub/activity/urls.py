from django.urls import path, include
from rest_framework import routers
from .views import ReviewApiView, FavoriteApiView

router = routers.DefaultRouter()
router.register("reviews", ReviewApiView, "reviews")
router.register("favorites", FavoriteApiView, "favorites")


urlpatterns = [
    path('', include(router.urls)),
]
