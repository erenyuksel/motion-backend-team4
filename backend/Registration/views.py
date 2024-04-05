from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import status, serializers
from rest_framework.generics import (CreateAPIView, GenericAPIView, get_object_or_404)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Registration.models import RegistrationProfile
from Registration.serializers import RegistrationEmailSerializer, VerificationCodeSerializer

User = get_user_model()


class RegistrationEmailSender(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationEmailSerializer
    permission_classes = []

    def perform_create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            email = serializer.validated_data.get('email')
            user, created = User.objects.get_or_create(email=email, username=email, is_active=False)

            send_mail(
                'Motion registration code',
                f'Here is your code for registration: {user.registration_profile.code}',
                'team.4.motion.project@gmail.com',
                [user.email],
                fail_silently=False,
            )
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'User already exists.'})

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RegistrationValidationAPIView(GenericAPIView):
    queryset = RegistrationProfile.objects.all()
    serializer_class = VerificationCodeSerializer
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # registration_profile = get_object_or_404(RegistrationProfile, pk=request.data['email'])
        registration_profile = get_object_or_404(RegistrationProfile, user__email=request.data['email'])
        # registration_profile = get_object_or_404(RegistrationProfile, user__email=request.query_params['email'])

        serializer.is_valid(raise_exception=True)
        if not serializer.validated_data['code'] == registration_profile.code:
            raise serializers.ValidationError("Registration code is not correct")


        user, created = User.objects.update_or_create(
            email=serializer.validated_data['email'],
            defaults={
                'first_name': serializer.validated_data['first_name'],
                'last_name': serializer.validated_data['last_name'],
                'username': serializer.validated_data['username'],
                # Set password and any other fields you need to update or set for new records
            }
        )

        user.set_password(serializer.validated_data['password'])
        user.save()

        # serializer.save()
        return Response(serializer.data)

