from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "genre"


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, unique=True)
    genres = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publish_date = models.DateField()

    def __str__(self):
        return self.title


    class Meta:
        db_table = "book"
