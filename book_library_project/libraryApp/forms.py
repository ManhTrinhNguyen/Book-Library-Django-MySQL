from .models import Book, Author
from django import forms

class BookForm(forms.ModelForm):
  class Meta:
    model = Book 
    fields = ['title', 'author' ,'genre', 'publish_date']


class AuthorForm(forms.ModelForm):
  class Meta:
    model = Author
    fields = ['name']