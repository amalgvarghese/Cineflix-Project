from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    USER = 'User','User'

    ADMIN = 'Admin','Admin'

class Profile(AbstractUser):

    role = models.CharField(max_length=10,choices=RoleChoices.choices)

    phone = models.CharField(null=True,blank=True)


    class Meta :

        verbose_name = 'Profiles'

        verbose_name_plural = 'Profiles'
        

    def __str__(self):

        return f'{self.username}'

