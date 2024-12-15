from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(default='Лошадка', max_length=100)
    last_name = models.CharField(default='Таинственная', max_length=100)
    age = models.IntegerField(default=0)
    work = models.CharField(default='', max_length=200)
    special = models.CharField(default='', max_length=200)
    status = models.CharField(default='', max_length=100)
