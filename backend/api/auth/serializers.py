from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from django.contrib.auth import login, logout, authenticate


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        request = self.context['request']
        logout(request)
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        if not username and not email:
            raise ValidationError('Requires username or email.')
        if username:
            user = authenticate(username=username, password=password)
        else:
            query = User.objects.filter(email=email)
            if not query:
                raise NotFound(f'{email} has no account.')
            username = query.first().username
            user = authenticate(username, password)
        if not user:
            raise AuthenticationFailed('Incorrect username or password.')
        login(self.context['request'], user)
        return user


class LogoutSerializer(serializers.Serializer):
    detail = serializers.CharField(read_only=True, default="Success")

class LoggedInSerializer(serializers.Serializer):
    detail = serializers.BooleanField(read_only=True, default=False)
