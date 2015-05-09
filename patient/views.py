from django.shortcuts import render

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.order_by
