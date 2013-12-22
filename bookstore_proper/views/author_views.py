from django.http import HttpResponse
from django.shortcuts import render_to_response
from bookstore_proper.models import Author

def show(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = author.book_set.all()
    return render_to_response('authors/show.html', locals())
