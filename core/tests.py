import json

from django.test import Client, TestCase
from django.urls import reverse

from .models import Book


class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.book1 = Book.objects.create(
            title="Test Book 1",
            authors="Test Author 1",
            ISBN="1234567890",
            description="This is test book 1",
        )
        self.book2 = Book.objects.create(
            title="Test Book 2",
            authors="Test Author 2",
            ISBN="0987654321",
            description="This is test book 2",
        )

    def test_get_book_list(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_add_book(self):
        data = {
            "title": "Test Book 3",
            "authors": "Test Author 3",
            "ISBN": "5432167890",
            "description": "This is test book 3",
        }
        response = self.client.post("/api/books/", data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 3)

    def test_get_book_detail(self):
        response = self.client.get(f"/api/books/{self.book1.ISBN}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Test Book 1")

    def test_update_book(self):
        data = json.dumps({"description": "Updated Description of test book 1"})
        headers = {"Content-Type": "application/json"}
        response = self.client.patch(
            f"/api/books/{self.book1.ISBN}/", headers=headers, data=data
        )
        self.assertEqual(response.status_code, 200)
        updated_book = Book.objects.get(ISBN=self.book1.ISBN)
        self.assertEqual(updated_book.description, "Updated Description of test book 1")

    def test_delete_book(self):
        response = self.client.delete(f"/api/books/{self.book1.ISBN}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(ISBN=self.book1.ISBN).exists())
