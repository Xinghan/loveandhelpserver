from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, views
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrTargetUser
from .serializers import UserSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        if self.request.method == 'POST':
           return (AllowAny(),)
        else:
           return (IsStaffOrTargetUser(),)
