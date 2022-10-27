from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=700)
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=700, required=False)
    password = serializers.CharField(max_length=700)
    email = serializers.CharField(max_length=700, required=False)
    
    def validate(self, attrs):
        if attrs.get('username') is None and attrs.get('email') is None:
            raise ValidationError(detail={"message": "Please enter a username or email address"})
        
        return super().validate(attrs)
    