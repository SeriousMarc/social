from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from users import serializers
from .models import User

class UserViewSet(viewsets.ModelViewSet):   
    queryset = User.objects.all()
    serializer_class = serializers.UserCreationSerializer
    permission_classes = (AllowAny,)
