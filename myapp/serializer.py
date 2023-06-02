from rest_framework import serializers
from .models import *
###Atagulyyew Suwhan
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User1
        fields=('id','email','number')

