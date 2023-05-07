from django.contrib.auth.models import AbstractUser
from django.db import models

#inherit all the fields and methods of the AbstractUser class
class User(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    class Meta:
        db_table = 'user'
