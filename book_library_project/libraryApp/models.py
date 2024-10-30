from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name 
  

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
  genre = models.CharField(max_length=50)
  publish_date = models.DateField()

  def __str__(self):
    return f'Book {self.title} by {self.author}'
  
  

  
