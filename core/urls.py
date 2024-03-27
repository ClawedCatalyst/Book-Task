from django.urls import path

from . import views

urlpatterns = [
    path("api/books/", views.BookListView.as_view(), name="book-list"),
    path("api/books/<isbn>/", views.BookDetailView.as_view(), name="book-detail"),
]
