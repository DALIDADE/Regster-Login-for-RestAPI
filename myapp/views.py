from django.shortcuts import render
from .models import UserNew
from rest_framework import generics,status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializers

class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializers
    def post(self,request):
        email = request.data.get('email')
        number = request.data.get('number')
        if UserNew.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        elif UserNew.objects.filter(number=number).exists():
            return Response({'error': 'number already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = UserNew.objects.create_user(number=number, email=email)
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'email': email}, status=status.HTTP_201_CREATED)