from django.contrib import admin
from .models import Employee

# Register your models here.
admin.site.register(Employee)

# can also set up seeds for db here