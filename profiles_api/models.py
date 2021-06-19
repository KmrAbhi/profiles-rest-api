from django.db import models
from django.cotrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin

# Create your models here.

class userProfile(AbstractBaseUser , PermissionMixin):
    """Database Model For Users In The System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FILEDS = ['name']

    def get_full_name(self):
        """Retrieve Full Name of User"""
        return self.name

    def get_shor_name(self):
        """Return Short Name of User"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
        


