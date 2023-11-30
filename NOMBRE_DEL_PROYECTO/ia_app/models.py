# Create your models here.
from django.db import models

class DatabaseConfiguration(models.Model):
    name = models.CharField(max_length=255, unique=True)
    odbc_driver = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    database = models.CharField(max_length=255)
    trusted_connection = models.BooleanField(default=True)
    login_timeout = models.IntegerField(default=30)
    encrypt = models.BooleanField(default=False)

    def __str__(self):
        return self.name
