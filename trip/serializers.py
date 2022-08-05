from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import UserProfile , Trip


User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    #for token
    access =serializers.CharField(allow_blank=True, read_only=True)
    
    def validate(self, data):
        username = data.get ("username")
        password = data.get("password")
        try:
            user = User.objects.get(username=username) #does user exist in my database?
        except User.DoesNotExist:
            raise serializers. ValidationError ("Looks like user doesn't exist.. ")
        if not user.check_password(password):
            raise serializers.ValidationError ("Looks like password is incorrect..")
        
        #token code here
        
        payload = RefreshToken.for_user(user)
        token = str(payload.access_token)
        
        data["access"] = token
        
        return data


"""When the user registers an account, the backend should automatically create an empty Profile
associated with this new User account. The user should not have to create a Profile.
My profile has my profile image, bio, and total number of trips. Total number of trips
should not be stored in the database, it should be calculated in the frontend.
Feel free to add more fields."""

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password","first_name","last_name","email"]
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data

"""After Creating a user, the backend should automatically create an empty Profile"""
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user","first_name","last_name","bio","avatar","total_trips","list_of_trips"]
        extra_kwargs = {
            "user": {"read_only": True}
        }



"""As a user, I can create a new trip."""

class TripCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["title", "description", "image", "country", "like", "wants_to_visit"]
    def create(self, validated_data):
        title = validated_data["title"]
        description = validated_data["description"]
        image = validated_data["image"]
        country = validated_data["country"]
        like = validated_data["like"]
        wants_to_visit = validated_data["wants_to_visit"]
        new_trip = Trip(title=title, description=description, image=image, country=country, like=like, wants_to_visit=wants_to_visit)
        new_trip.save()
        return validated_data