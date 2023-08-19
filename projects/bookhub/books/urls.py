from django.urls import path, include
from rest_framework import routers
from .views import BookApiView, GenreApiView, AuthorApiView

router = routers.DefaultRouter()
router.register("genres", GenreApiView, "genres")
router.register("authors", AuthorApiView, "authors")
router.register("", BookApiView, "books")


urlpatterns = [
    path('', include(router.urls)),
]
