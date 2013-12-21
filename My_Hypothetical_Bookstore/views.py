from django.http import HttpResponse
from django.shortcuts import render_to_response
from bookstore_proper.models import Book
import datetime

def home(request):
    current_date = datetime.datetime.now()
    return render_to_response('home.html', locals())

def books(request):
    books = Book.objects.all()
    return render_to_response('books/index.html', locals())

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    attributes = book.__dict__.items()
    print(attributes)
    return render_to_response('books/show.html', locals())
