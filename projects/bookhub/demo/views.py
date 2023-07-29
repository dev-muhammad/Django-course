import json
from django.views import View
from django.http.response import JsonResponse

from .models import Book

class BooksView(View):

    def get(self, request):

        all_books = Book.objects.all()
        books = []
        for book in all_books:
            books.append(
               {
                   "name": bytes(book.name, "utf-8").decode("unicode_escape"),
                   "pages": book.pages,
                   "publish_year": book.publish_year,
               } 
            )
        data = {"books":books}
        return JsonResponse(data=data)
    
    def single(self, book_id):
        book = Book.objects.get(pk = book_id)
        if book:
            book = {
                    "name": bytes(book.name, "utf-8").decode("unicode_escape"),
                    "pages": book.pages,
                    "publish_year": book.publish_year,
                }
            return JsonResponse(data=book)
        else:
            return JsonResponse(data={"error":"book not found"})
    
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        publisher = data.get('publisher')
        publish_year = data.get('publish_year')
        author_id = data.get('author_id')
        pages = data.get('pages')
        new_book = Book.objects.create(
            name = name,
            publisher = publisher,
            publish_year = publish_year,
            author_id = author_id,
            pages = pages
        )
        return JsonResponse(data={"status":"Success", "id": new_book.id})
