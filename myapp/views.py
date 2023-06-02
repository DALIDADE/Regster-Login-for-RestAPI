from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
###Atagulyyew Suwhan
class UserRegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        number = serializer.validated_data['number']
        try:
            user = User1.objects.get(email=email)
            return Response({'error': 'A user with this email already exists.'}, status=400)
        except User1.DoesNotExist:
            pass

        try:
            user = User1.objects.get(number=number)
            return Response({'error': 'A user with this number already exists.'}, status=400)
        except User1.DoesNotExist:
            pass

        user = User1(email=email, number=number)
        user.generate_token()
        user.save()
        token = user.token
        return Response({'token': token, 'user': email, 'number': number})


class UserLoginView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        number = serializer.validated_data['number']
        try:
            user = User1.objects.get(email=email, number=number)
        except User1.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        token = user.token
        return Response({'token': token, 'user': email, 'number': number})


