from pickle import GET
from django.shortcuts import render
from rest_framework import generics
from .models import Book, Tracking, Note
from .serializers import BookSerializer, TrackingSerializer, NoteSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class FeaturedBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(featured=True)
        return queryset


class TrackingList(generics.ListCreateAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Tracking.objects.filter(user=self.request.user)
        return queryset


class TrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user)
        return queryset


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class PublicNote (generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.filter(privacy=False)
        return queryset


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'library': reverse('library-list', request=request, format=format),
        'tracking': reverse('tracking-list', request=request, format=format),
        'notes': reverse('notes-list', request=request, format=format)
    })
