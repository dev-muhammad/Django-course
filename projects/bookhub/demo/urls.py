from django.urls import path
from .views import BooksView

urlpatterns = [
    path('all/', BooksView.as_view(), name='books'),
    path('<int:book_id>/', BooksView.single, name='books-single'),
]
