from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
