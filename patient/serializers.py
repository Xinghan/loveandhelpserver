from rest_framework import serializers
from patient.models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient
        fields = ('name', 'age', 'owner')
        
