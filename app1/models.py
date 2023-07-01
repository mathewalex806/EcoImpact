from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.username}"
    
class Airtravel(models.Model):
    name = models.CharField(max_length=100 , default="", blank=True , null=True)
    attributes = models.CharField(max_length=300)
    description = models.CharField(default='', blank=True, null=True , max_length=500)
    def __str__(self):
        return f"{self.name}"
    
class Roadtravel(models.Model):
    name = models.CharField(max_length=100 , default="", blank=True , null=True)
    attributes = models.CharField(max_length=300)
    description = models.CharField(default='', blank=True, null=True , max_length=500)
    def __str__(self):
        return f"{self.name}"
    
class Seatravel(models.Model):
    name = models.CharField(max_length=100 , default="", blank=True , null=True)
    attributes = models.CharField(max_length=300)
    description = models.CharField(default='', blank=True, null=True , max_length=500)
    def __str__(self):
        return f"{self.name}"
    
class Info(models.Model):
    name = models.CharField(max_length=100 , default="", blank=True , null=True)
    attributes = models.CharField(max_length=300)
    description = models.CharField(default='', blank=True, null=True , max_length=500)
    def __str__(self):
        return f"{self.name}"
    
class Energy(models.Model):
    name = models.CharField(max_length=100 , default="", blank=True , null=True)
    attributes = models.CharField(max_length=300)
    description = models.CharField(default='', blank=True, null=True , max_length=500)
    def __str__(self):
        return f"{self.name}"

class Goods(models.Model):
    name = models.CharField(max_length=100 , default="", blank=True , null=True)
    attributes = models.CharField(max_length=300)
    description = models.CharField(default='', blank=True, null=True , max_length=500)
    def __str__(self):
        return f"{self.name}"
    
