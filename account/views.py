from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .permissions import IsStaffOrTargetUser
from .serializers import UserSerializer
from . import authentication, serializers
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

class AuthView(views.APIView):
    authentication_classes = (BasicAuthentication,)
    
    serializer_class = serializers.UserSerializer
    
    def post(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)
    
