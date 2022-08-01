from django.shortcuts import render
import datetime
from rest_framework import generics
from trip import serializers

# Create your views here.

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserCreateSerializer