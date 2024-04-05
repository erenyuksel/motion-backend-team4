from django.urls import path
from User.views import ListCreateUserView

api_user_patterns = [
    path('users/', ListCreateUserView.as_view()),
    # path('users/<int:user_id>/', .as_view()),
]
