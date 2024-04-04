from django.urls import path

from Registration.views import RegistrationEmailSender

urlpatterns = [path('', RegistrationEmailSender.as_view())]
