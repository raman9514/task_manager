from rest_framework import serializers
from .models import User

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)  # Hide password in response
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile' ,'password']
        
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
        ) # Create Use  
        user.set_password(validated_data['password'])  # Hash & Set Passwprd
        user.save()
        return user