from django.urls import path, include
from rest_framework import routers
from .views import BadBooksView, BookApiView, BookGenericApiView

router = routers.DefaultRouter()
router.register("", BookGenericApiView, "generic")


urlpatterns = [
    path('', include(router.urls)),
    # path('api/', BookApiView.as_view(), name='api-books'),
    # path('all/', BadBooksView.as_view(), name='books'),
    # path('<int:book_id>/', BadBooksView.single, name='books-single'),
]
