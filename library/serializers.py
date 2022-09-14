from rest_framework import serializers
from .models import Book, Tracking, Note


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date',
                  'genre', 'featured')


class TrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracking
        fields = ('status', 'user', 'book')


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('user', 'book', 'date_created',
                  'notes', 'privacy', 'page_number')
