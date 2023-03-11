from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create Profile Model


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    mob_phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars/',
                               default='default_avatar.png')

    def __str__(self):
        return str(self.user)
