from django.urls import path
from .views import BadBooksView, BookApiView

urlpatterns = [
    path('api/', BookApiView.as_view(), name='api-books'),
    path('all/', BadBooksView.as_view(), name='books'),
    path('<int:book_id>/', BadBooksView.single, name='books-single'),
]
