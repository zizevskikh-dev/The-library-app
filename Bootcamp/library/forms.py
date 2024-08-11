from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Введите ФИО автора',
            'books': 'Выберите книгу(-и) автора из списка',
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Введите название книги',
        }
