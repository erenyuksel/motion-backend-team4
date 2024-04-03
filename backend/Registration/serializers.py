from rest_framework import serializers


class RegistrationEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, required=True)
