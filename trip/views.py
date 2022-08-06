from cgitb import lookup
from django.shortcuts import render
import datetime
from rest_framework import generics
from trip import serializers
from trip import models
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner, IsNotTooSoon
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model



"""Register useing the a new user and response with token called "access" """


# Create your views here.

"""While Creating a User profile the following fields are required: 
1- id
2- username
3- password
4- First Name
5- Last Name
6- image

and token would be generated for the user"""

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserCreateSerializer

"""After Creating a user, the backend should automatically create an empty Profile"""
class UserProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

"""While Creating a Trip the following fields are required:
1- id
2- title
3- description
4- image
5- country
6- like
7- wants_to_visit"""

class TripCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.TripCreateSerializer
    permission_classes = [IsAuthenticated]

"""Update Trip (only by owner)"""

class TripUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.TripCreateSerializer
    queryset = models.Trip.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"
    permission_classes = [IsAuthenticated, IsOwner]



 
"""Delete Trip (only by owner)"""

class TripDeleteAPIView(generics.DestroyAPIView):
    serializer_class = serializers.TripCreateSerializer
    queryset = models.Trip.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"
    permission_classes = [IsAuthenticated, IsOwner]

"""List all Trips
Create a screen called "Explore" where the user can view all trips.
"Explore" screen should not display the description of the trip.
Trips have an id, title, description, and image."""

class TripListAPIView(generics.ListAPIView):
    serializer_class = serializers.TripCreateSerializer
    permission_classes = [AllowAny]
    queryset = models.Trip.objects.all()


"""As a user, I can press on the owner of a trip to view their profile
Display the name of the owner of a trip for every trip on the app.
This allows the user to view every other trip made by the same owner."""

# class UserProfileListAPIView(generics.ListAPIView):
