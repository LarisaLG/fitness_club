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


# Trainers
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mob_phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_joined = models.DateField()
    profile_avatar = models.ImageField(upload_to='trainer_avatars/',
                                       default='trainer_avatar.png')
    specialization = models.ForeignKey('Specialization',
                                       on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name


# Trainer specialization
class Specialization(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
