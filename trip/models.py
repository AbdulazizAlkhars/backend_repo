from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

"""When the user registers an account, the backend should automatically create an empty Profile
associated with this new User account. The user should not have to create a Profile.
My profile has my profile image, bio, and total number of trips. Total number of trips
should not be stored in the database, it should be calculated in the frontend.
Feel free to add more fields.

also add a list of trip who are going to visit
"""

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    bio = models.TextField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to='images', blank=False, default='/Users/ahmadcoded/Development/project/Travel_App/backend_repo/media/images/Simulator_Screen_Shot_-_iPhone_13_Pro_Max_-_2022-06-22_at_17.46.04.png')
#    total_trips = models.IntegerField(default=0)
    list_of_trips = models.ManyToManyField('Trip', blank=True)
    def __str__(self):
        return self.user.username



"""User has to enter the `title`, `description`, and `image` of the trip.
When creating a trip, automatically assign the logged-in user as the `owner` of this trip.
This means that the `Trip` model also needs an `owner` relationship field with the `User` model.
trip_id (int)
title (str)
description (str)
image (str)
Name of the country (string)
Like (boolean)
Wants to visit (boolean)

"""



class Trip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default=True)
    description = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images', blank=True, default='/Users/ahmadcoded/Development/project/Travel_App/backend_repo/media/images/Simulator_Screen_Shot_-_iPhone_13_Pro_Max_-_2022-06-22_at_17.46.04.png')
    country = models.CharField(max_length=100, default=True)
    like = models.BooleanField(default=False)
    wants_to_visit = models.BooleanField(default=False)
    def __str__(self):
        return self.title

s