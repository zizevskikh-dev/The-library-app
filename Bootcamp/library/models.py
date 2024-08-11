from django.db import models
# from .validators import validate_spaces


class Book(models.Model):
    title = models.TextField(unique=True, null=False, blank=False)

    def __str__(self):
        return f'#{self.pk} {self.title}'


class Author(models.Model):
    name = models.TextField(unique=True, null=False, blank=False)
    books = models.ManyToManyField(Book, related_name='authors')
