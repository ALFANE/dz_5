from django.db import models

# Create your models here.
class Student(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null = True)
    surname = models.CharField(max_length=200, null = True)
    age = models.IntegerField(null = True)
    sex = models.CharField(max_length=2, null = True)
    address = models.CharField(max_length=100, null = True)
    description = models.TextField(max_length=500, null = True)
    birthday = models.DateField(null = True)
    email = models.EmailField(null = True)

