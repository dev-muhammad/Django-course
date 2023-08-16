from django.urls import path, include
from rest_framework import routers
from .views import BookApiView, GenreApiView, AuthorApiView

router = routers.DefaultRouter()
router.register("", BookApiView, "books")
router.register("genres", GenreApiView, "genres")
router.register("authors", AuthorApiView, "authors")


urlpatterns = [
    path('', include(router.urls)),
]
