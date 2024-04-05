from rest_framework import serializers

from .models import User


class RegistrationEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, required=True)


class VerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=40, required=True)
    code = serializers.CharField(max_length=5, write_only=True)
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
