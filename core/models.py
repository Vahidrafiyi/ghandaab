from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Profile(models.Model):
    ADMIN = 0
    AUTHOR = 1
    USER = 2

    USER_ROLE = (
        (ADMIN, 'Admin'),
        (AUTHOR, 'Author'),
        (USER, 'User'),
    )

    MALE = 0
    FEMALE = 1

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    user      = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    image     = models.ImageField(upload_to='images/profiles/',
                              null=True,
                              blank=True)
    phone     = models.CharField(max_length=14)
    gender    = models.PositiveSmallIntegerField(choices=GENDER, default=0)
    user_role = models.PositiveSmallIntegerField(choices=USER_ROLE, default=2)

    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.email

    def clean(self):
        if self.gender > 1:
            raise ValidationError('please enter 0 or 1 \n 0 : male , 1 : female')
        if self.user_role > 2: 
            raise ValidationError('please enter number between 0 to 2 \n 0 : admin , 1 : author , 2 : user')

