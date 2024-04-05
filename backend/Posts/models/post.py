from django.db import models
from motion_project import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField('Comment', related_name='post_comments', blank=True)
    images = models.ManyToManyField('Image', related_name='post_images', blank=True)
    shared_posts = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='shares')
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Post {self.id} by {self.author.username}"
