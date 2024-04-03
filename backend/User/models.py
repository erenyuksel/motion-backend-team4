from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class CustomUserManager(BaseUserManager):
#
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(email, password, **extra_fields)
#

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, blank=False, max_length=100)
    password = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    first_name = models.CharField(max_length=150, blank=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    # banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # liked_posts = models.ManyToManyField('Posts', related_name='liked_by', blank=True)
    # posts = models.ManyToManyField('Posts', related_name='author', blank=True)
    # comments = models.ManyToManyField('Comments', related_name='commented_by', blank=True)
    # registration_profile = models.OneToOneField('Registration', on_delete=models.CASCADE, related_name='user')
    # followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    # friend_requests_sent = models.ManyToManyField('Friends', related_name='sender', blank=True)
    # friend_requests_received = models.ManyToManyField('Friends', related_name='receiver', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    # objects = CustomUserManager()

    def __str__(self):
        return self.email
