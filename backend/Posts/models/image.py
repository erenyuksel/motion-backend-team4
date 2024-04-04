from django.db import models


class Image(models.Model):
    image = models.CharField(max_length=255)
    post = models.ForeignKey('Post', related_name='post_images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for post {self.post.id}"
