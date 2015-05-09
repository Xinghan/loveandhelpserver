from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    birthday = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return self.user.encode('utf-8')

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User profiles"
