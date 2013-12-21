from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'My_Hypothetical_Bookstore.views.home', name='home'),
    url(r'^books/$', 'My_Hypothetical_Bookstore.views.books', name='books_index'),
    url(r'^books/(?P<book_id>\d+)/$', 'My_Hypothetical_Bookstore.views.book', name='book_show'),
    url(r'^admin/', include(admin.site.urls)),
)
