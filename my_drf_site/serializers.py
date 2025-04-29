from .models import Book
from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
