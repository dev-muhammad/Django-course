from django.urls import path, include
from rest_framework import routers

from my_app.views import BookViewSet, Book1ViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet, "books")
router.register("other", Book1ViewSet, "other")

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]