from django.urls import path, include
from rest_framework import routers

from my_app.views import BookViewSet, Book1ViewSet, ClassBasedView, function_based_view, MyBookViewSet

router = routers.DefaultRouter()
router.register("my-books", MyBookViewSet, "my-books")
router.register("books", BookViewSet, "books")
router.register("other", Book1ViewSet, "other")

urlpatterns = [
    path('', include(router.urls)),
    path('function', function_based_view, name='function_based_view'),
    path('class', ClassBasedView.as_view(), name='ClassBasedView'),
]
