from django.urls import path

from .views import GenreListView, GenreDetail, AuthorListView, AuthorDetailView, BookListView, BookDetail

urlpatterns = [
    path('genre/', GenreListView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetail.as_view(), name='genre_detail'),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('book/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail')
]