from django.db import models

# Create your models here.
class Student(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=2)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    birthday = models.DateField()
    email = models.EmailField()

