from rest_framework import serializers
from .models import Post, Comment, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'created', 'likes_count']


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    shares_count = serializers.IntegerField(source='shared_posts.count', read_only=True)
    likes_count = serializers.IntegerField(source='liked_by.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'description', 'created', 'updated', 'author', 'shared_posts', 'liked_by', 'images', 'comments', 'shares_count', 'likes_count']
        read_only_fields = ['author', 'created', 'updated']

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj)
        return CommentSerializer(comments, many=True, read_only=True, context=self.context).data