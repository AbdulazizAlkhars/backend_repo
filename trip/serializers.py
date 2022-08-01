from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

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

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password","first_name","last_name"]
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data