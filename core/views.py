from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookListView(
    generics.CreateAPIView,
    generics.ListAPIView,
):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def post(self, request):
        return self.create(request)


class BookDetailView(
    generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = BookSerializer

    def get(self, request, isbn):
        book = get_object_or_404(Book, isbn=isbn)
        serializer = self.serializer_class(book, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, isbn):
        book = get_object_or_404(Book, isbn=isbn)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
