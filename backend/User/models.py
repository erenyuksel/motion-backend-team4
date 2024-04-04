from django.db import models
from django.contrib.auth.models import  AbstractUser
from motion_project import settings

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, max_length=100)
    password = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    first_name = models.CharField(max_length=150, blank=False)
    username = models.CharField(max_length=150, blank=False)
    phone = models.CharField(max_length=15, blank=True, null=True)

    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    # banner = models.ImageField(upload_to='banners/', blank=True, null=True)

    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # liked_posts = models.ManyToManyField('Posts', related_name='liked_by', blank=
    # posts = models.ManyToManyField('Posts', related_name='author', blank=True)
    # comments = models.ManyToManyField('Comments', related_name='commented_by', blank=True)

    # friend_requests_sent = models.ManyToManyField('Friends', related_name='sender', blank=True)
    # friend_requests_received = models.ManyToManyField('Friends', related_name='receiver', blank=True)

    following = models.ManyToManyField(
        verbose_name='following',
        to=settings.AUTH_USER_MODEL,
        related_name='followers',
        blank=True
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # objects = CustomUserManager()

    def __str__(self):
        return self.email
