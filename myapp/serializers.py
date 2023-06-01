from rest_framework import serializers
from .models import UserNew

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserNew
        fields=('id','email','number','password')
        def create(self, validated_data):
            email = validated_data['email']
            number = validated_data['number']
            user = UserNew.objects.create(**validated_data)
            return user
