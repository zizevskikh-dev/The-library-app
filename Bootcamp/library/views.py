from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .forms import AuthorForm, BookForm
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class LibraryHomePageView(TemplateView):
    template_name = 'library/library-home-page.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('library:authors_list')


class AuthorListView(ListView):
    queryset = Author.objects.all()


class AuthorDetailsView(DetailView):
    queryset = Author.objects.all()


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('library:authors_details', kwargs={'pk': self.object.pk})


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('library:authors_list')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('library:books_list')


class BookListView(ListView):
    queryset = Book.objects.all()


class BookDetailsView(DetailView):
    queryset = Book.objects.all()


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('library:books_details', kwargs={'pk': self.object.pk})


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('library:books_list')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
