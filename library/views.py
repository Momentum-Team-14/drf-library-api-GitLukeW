from pickle import GET
from django.shortcuts import render
from rest_framework import generics
from .models import Book, Tracking, Note
from .serializers import BookSerializer, TrackingSerializer, NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TrackingList(generics.ListCreateAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer


class TrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'library': reverse('library-list', request=request, format=format),
        'tracking': reverse('tracking-list', request=request, format=format),
        'notes': reverse('notes-list', request=request, format=format)
    })
