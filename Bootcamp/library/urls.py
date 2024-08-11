from django.urls import path, include
from rest_framework import routers
from .views import *


app_name = "library"
author_router = routers.SimpleRouter()
author_router.register(r'author', AuthorViewSet)
book_router = routers.SimpleRouter()
book_router.register(r'book', BookViewSet)

urlpatterns = [
    path('', LibraryHomePageView.as_view(), name='library_home_page'),
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('authors/create/', AuthorCreateView.as_view(), name='authors_create'),
    path('authors/<int:pk>/', AuthorDetailsView.as_view(), name='authors_details'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='authors_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='authors_delete'),
    path('books/', BookListView.as_view(), name='books_list'),
    path('books/create/', BookCreateView.as_view(), name='books_create'),
    path('books/<int:pk>/', BookDetailsView.as_view(), name='books_details'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='books_delete'),
    path('api/v1/', include(author_router.urls)),
    path('api/v1/', include(book_router.urls)),
]
