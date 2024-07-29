from rest_framework import serializers
from .models import Book, Genre, Author


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genres = GenreSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validate_data):
        author_data = validate_data.pop('author')
        author, create = Author.objects.get_or_create(author_data)
        genre_data = validate_data.pop('genres')
        genre, create = Genre.objects.get_or_create(genre_data)
        book = Book.objects.create(author=author, genres=genre, **validate_data)
        return book

    def update(self, instance, validate_data):
        author_data = validate_data.pop('author')["name"].lower()

        author, create = Author.objects.get_or_create(name=author_data)
        genre_data = validate_data.pop('genres')["name"]
        instance.publish_date = validate_data.pop('publish_date')
        genre, create = Genre.objects.get_or_create(name=genre_data)
        instance.author = author
        instance.genres = genre

        instance.save()
        return instance
