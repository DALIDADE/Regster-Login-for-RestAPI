from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import jwt

###Atagulyyew Suwhan

class User1(models.Model):
    email =models.EmailField()
    number = models.PositiveIntegerField()
    token = models.CharField(max_length=255, blank=True)

##create token 
    def generate_token(self):
        payload = {
            'email': self.email,
            'number': self.number
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        self.token = token
        self.save()
###create token end
    def __str__(self):
        return self.email


