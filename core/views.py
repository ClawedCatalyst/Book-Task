from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookListView(
    generics.CreateAPIView,
    generics.ListAPIView,
):
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination

    def get(self, request):
        books = Book.objects.all()

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_response = paginator.paginate_queryset(books, request)

        serializer = self.serializer_class(paginated_response, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        return self.create(request)


class BookDetailView(
    generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = BookSerializer

    def get(self, request, isbn):
        book = get_object_or_404(Book, ISBN=isbn)
        serializer = self.serializer_class(book, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, isbn):
        book = get_object_or_404(Book, ISBN=isbn)
        serializer = self.serializer_class(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, isbn):
        book = get_object_or_404(Book, ISBN=isbn)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
