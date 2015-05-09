from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrTargetUser

# Create your views here.

class UserView(viewsets.ModelsViewSet):
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser())
