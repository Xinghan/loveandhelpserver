from django.contrib.auth.models import User
from rest_framework import serializers
from patient.models import Patient

class UserSerializer(serializers.ModelSerializer):
    patients = serializers.PrimaryKeyRelatedField(many=True, queryset=Patient.objects.all())
    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'email')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
