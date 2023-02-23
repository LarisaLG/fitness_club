from django.db import models

# Create your models here.

# Package pricing


class Package(models.Model):

    class Meta:
        """"
        Shows you a user friendly name in the admin.
        """

        verbose_name_plural = 'Packages'

    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


# Package details

class PackDetail(models.Model):
    package = models.ForeignKey(Package, related_name='Classes',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    included = models.BooleanField(default=False)

    def __str__(self):
        return self.title
