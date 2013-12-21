from django.http import HttpResponse
from django.shortcuts import render_to_response
from bookstore_proper.models import Book
import datetime

def home(request):
    current_date = datetime.datetime.now()
    books = Book.objects.all()
    return render_to_response('home.html', locals())
