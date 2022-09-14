from rest_framework import serializers
from .models import Book, CustomUser, Tracking


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date',
                  'genre', 'featured')


class TrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracking
        fields = ('status', 'user', 'book')


class CustomUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CustomUser
        fields = ('id', 'username')
