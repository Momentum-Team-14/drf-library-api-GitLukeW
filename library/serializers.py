from rest_framework import serializers
from .models import Book, Tracking, Note


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date',
                  'genre', 'featured')


class TrackingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
         slug_field="username", read_only=True)
    book = serializers.SlugRelatedField(
         slug_field="title", read_only=True)

    class Meta:
        model = Tracking
        fields = ('status', 'user', 'book', 'id')


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
         slug_field="username", read_only=True)
    book = serializers.SlugRelatedField(
         slug_field="title", read_only=True)

    class Meta:
        model = Note
        fields = ('user', 'book', 'date_created',
                  'notes', 'privacy', 'page_number')
