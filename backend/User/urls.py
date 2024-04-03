from django.urls import path

from User.views import ListCreateUserView

# from backend.User.views import ListCreateUserView

# from user.views import ListCreateUserView, ListCreateFollowersView, ListCreateFollowingView

urlpatterns = [
    path('create/', ListCreateUserView.as_view()),
    # path('backend/api/social/followers/followers/', ListCreateFollowersView.as_view()),
    # path('backend/api/social/followers/following/', ListCreateFollowingView.as_view()),
    # path('backend/api/social/followers/following/<int:id>/', ReadUpdateDeletePostView.as_view()),
]