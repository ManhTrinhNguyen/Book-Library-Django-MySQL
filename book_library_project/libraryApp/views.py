from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book
from .forms import AuthorForm, BookForm

# Create your views here.

def book_list(request):
  books = Book.objects.all()
  return render(request, 'book_list.html', {'books': books})

def create_book(request):
  form = BookForm()
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('books')
    
  return render(request, 'create_book.html', {'form': form})

def update_book(request, pk):
  book = get_object_or_404(Book, pk = pk)
  form = BookForm(instance=book)

  if request.method == 'POST':
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
      form.save()
      return redirect('books')
    
  return render(request, 'update_book.html', {'form': form})

def delete_book(request, pk):
  book = get_object_or_404(Book, pk = pk)
  if request.method == 'POST':
    book.delete()
    return redirect('books')
  return render(request, 'delete_book.html', {'book': book})


def create_auhor(request):
  form = AuthorForm()
  if request.method == 'POST':
    form = AuthorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('books')

  return render(request, 'create_author.html', {'form': form})



