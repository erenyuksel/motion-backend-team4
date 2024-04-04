from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework import generics, views, status
from rest_framework.response import Response
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly


# For creating a new post and listing all posts
class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        search_string = self.request.query_params.get('search', None)
        if search_string:
            queryset = queryset.filter(description__icontains=search_string)
        return queryset


# For retrieving, updating, and deleting a specific post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        post_id = self.kwargs.get("pk")
        post = get_object_or_404(Post, pk=post_id)
        return post


# For liking/unliking a post
class ToggleLikeView(views.APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if request.user in post.liked_by.all():
            post.liked_by.remove(request.user)
        else:
            post.liked_by.add(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


# For listing posts by a specific user
class UserPostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(author_id=user_id).order_by('-created')


# For listing posts from followed users (assuming a 'following' relationship exists on the User model)
class FollowingPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__followers__in=[user]).order_by('-created')


# For listing posts from friends (assuming a 'friends' relationship exists on the User model)
class FriendsPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__friends__in=[user]).order_by('-created')


# For listing posts liked by the logged-in user
class LikedPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(liked_by=user).order_by('-created')


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(user=self.request.user, post_id=post_id)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id).order_by('-created')
