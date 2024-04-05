from django.urls import path
from Posts.views import (
    PostCreateListView,
    PostDetailView,
    ToggleLikeView,
    UserPostListView,
    FollowingPostsListView,
    FriendsPostsListView,
    LikedPostsListView,
    CommentCreateView,
    CommentListView,
)

urlpatterns = [
    path('social/posts/', PostCreateListView.as_view(), name='create-list-posts'),
    path('social/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # pk for post_id
    path('social/posts/toggle-like/<int:post_id>/', ToggleLikeView.as_view(), name='toggle-like'),
    path('social/posts/user/<int:user_id>/', UserPostListView.as_view(), name='user-posts'),
    path('social/posts/following/', FollowingPostsListView.as_view(), name='following-posts'),
    path('social/posts/friends/', FriendsPostsListView.as_view(), name='friends-posts'),
    path('social/posts/likes/', LikedPostsListView.as_view(), name='liked-posts'),
    path('social/comments/<int:post_id>/', CommentListView.as_view(), name='comment-list'),
    path('social/comments/<int:post_id>/create/', CommentCreateView.as_view(), name='comment-create'),
]
