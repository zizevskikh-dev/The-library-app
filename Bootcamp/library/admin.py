from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
