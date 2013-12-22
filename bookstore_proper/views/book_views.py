from django.http import HttpResponse
from django.shortcuts import render_to_response
from bookstore_proper.models import Book

def index(request):
    books = Book.objects.all()
    return render_to_response('books/index.html', locals())

def show(request, book_id):
    book = Book.objects.get(pk=book_id)
    authors = book.authors.all()
    publisher = book.publisher
    publication_attributes = {"Publication Date": book.publication_date, "ISBN": book.isbn}.items()
    return render_to_response('books/show.html', locals())
