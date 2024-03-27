import uuid

from django.db import models


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publication_date = models.DateField(null=True, blank=True)
    ISBN = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"
