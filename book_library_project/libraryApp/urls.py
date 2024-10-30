from django.urls import path
from . import views 

urlpatterns = [
  path('books/', views.book_list, name = 'books'),
  path('books/newbook', views.create_book, name = 'create_book'),
  path('books/newauthor', views.create_auhor, name = 'create_author'),
  path('books/<int:pk>/edit', views.update_book, name = 'update_book'),
  path('books/<int:pk>/delete', views.delete_book, name = 'delete_book')
]