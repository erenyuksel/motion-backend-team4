# Create your views here.
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model
from User.serializers import UserSerializer

User = get_user_model()


# users/ GET: Get all the users
class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
