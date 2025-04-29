from django.shortcuts import render

from .serializers import UserSerializer,BookSerializers
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Book

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

