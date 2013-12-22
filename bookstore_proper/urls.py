from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bookstore_proper.views.application_views.home', name='home'),
    url(r'^books/$', 'bookstore_proper.views.book_views.index', name='books_index'),
    url(r'^books/(?P<book_id>\d+)/$', 'bookstore_proper.views.book_views.show', name='book_show'),
    url(r'^admin/', include(admin.site.urls)),
)
