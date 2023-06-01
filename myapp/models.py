from django.db import models
from django.contrib.auth.models import AbstractUser

class UserNew(AbstractUser):
    number = models.PositiveIntegerField(null=True, blank=True)

