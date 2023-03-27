from django.db import models


# Trainers
class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_joined = models.DateField()
    profile_avatar = models.ImageField(upload_to='trainer_avatars/',
                                       default='default_avatar.png')
    specialization = models.ForeignKey('Specialization',
                                       on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name


class Specialization(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
