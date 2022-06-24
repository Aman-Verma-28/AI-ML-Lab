from django.db import models

# Create your models here.
import datetime

class Reminder(models.Model):
    time = models.DateTimeField(auto_created=True)
    doctor = models.CharField(max_length=20)
    patient = models.CharField(max_length=20)
    link = models.CharField(max_length=20)
    doctor_id = models.CharField(max_length=20)
