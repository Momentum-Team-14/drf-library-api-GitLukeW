from pickle import GET
from django.shortcuts import render
from rest_framework import generics
from .models import Book, Tracking, CustomUser
from .serializers import BookSerializer, TrackingSerializer, CustomUserSerializer
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


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('user-list', request=request, format=format),
        'library': reverse('library-list', request=request, format=format),
        'tracking': reverse('tracking-list', request=request, format=format)
    })
