from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from Registration.serializers import RegistrationEmailSerializer

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
            user = User.objects.create(email=email, username=email, is_active=False)

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


