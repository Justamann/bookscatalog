from django.conf.urls import url
from mainapp import views

app_name = 'mainapp'
urlpatterns = [
    url(r'^catalog/', views.view_index, name='home'),
    url(r'^books/', views.BookListView.as_view(), name='books'),
    url(r'^authors/', views.AuthorsListView.as_view(), name='authors'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='book'),
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='author'),
    url(r'^registration/', views.get_name, name='registration'),
]
