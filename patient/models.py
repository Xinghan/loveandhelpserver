from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    cid = models.IntegerField()
    name = models.CharField(max_length=200);
    age = models.IntegerField();
    birthday = models.DateField()
    owner = models.ForeignKey(User, related_name='patients')

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
