from django.urls import path

from Registration.views import RegistrationEmailSender

# urlpatterns = [path('', RegistrationEmailSender.as_view())]


api_registration_patterns = [
    path('auth/registiration/', RegistrationEmailSender.as_view()),
    path('auth/registiration/validation/', RegistrationEmailSender.as_view()),
]
