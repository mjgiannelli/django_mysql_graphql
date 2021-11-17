from django.db import models

# Create your models here.
# class is equivalent to a table
# the keys are equivalent to a column
class Employee(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
