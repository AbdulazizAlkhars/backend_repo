from django.db import models
from django.contrib.auth.models import User 


# Create your models here.


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




class Trip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, default="")
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images',null=True ,blank=True, default='/Users/ahmadcoded/Development/project/Travel_App/backend_repo/media/images/Simulator_Screen_Shot_-_iPhone_13_Pro_Max_-_2022-06-22_at_17.46.04.png')
    country = models.CharField(max_length=100, null=True, default="")
    like = models.BooleanField(default=False, null=True)
    wants_to_visit = models.BooleanField(default=False, null=True)
    def __str__(self):
        return self.title
