from django.urls import path

from Registration.views import RegistrationEmailSender, RegistrationValidationAPIView

# urlpatterns = [path('', RegistrationEmailSender.as_view())]


api_registration_patterns = [
    path('auth/registration/', RegistrationEmailSender.as_view()),
    path('auth/registration/validation/', RegistrationValidationAPIView.as_view()),
]
