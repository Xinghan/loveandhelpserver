from django.db import models

# Create your models here.
class Patient(models.Model):
    cid = models.IntegerField()
    name = models.CharField(max_length=200);
    age = models.IntegerField();
    birthday = models.DateField()

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
