from django.shortcuts import render
from rest_framework import generics

from .models import CustomUser
from .serializers import RegisterSerializer


# Create your views here.



class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer