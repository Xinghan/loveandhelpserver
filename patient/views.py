from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.permissions import IsAuthenticated
 
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .permissions import IsOwner

# Create your views here.
class PatientView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_permissions(self):
        return (IsOwner(), )
