from django.test import TestCase
from my_app.models import Book


class BookModelTest(TestCase):

    def test_create_book(self):
        book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            cover_type="Hardcover",
            publish_year=2020,
        )
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "John Doe")
        self.assertEqual(book.cover_type, "Hardcover")
        self.assertEqual(book.publish_year, 2020)

    def test_str_representation(self):
        book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            cover_type="Hardcover",
            publish_year=2020,
        )
        self.assertEqual(str(book), "Test Book")

    def test_default_cover_type(self):
        book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publish_year=2020,
        )
        self.assertEqual(book.cover_type, "Paper")

    def test_create_time_auto_add(self):
        book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publish_year=2020,
        )
        self.assertIsNotNone(book.create_time)

    def test_update_time_auto(self):
        book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publish_year=2020,
        )
        initial_update_time = book.update_time

        book.title = "Updated Test Book"
        book.save()
        book.refresh_from_db()

        self.assertNotEqual(initial_update_time, book.update_time)

