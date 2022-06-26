from django.db import models

# Create your models here.
import datetime
from secrets import token_hex
from django.template.defaultfilters import slugify

class Reminder(models.Model):
    time = models.DateTimeField(auto_created=True)
    doctor = models.CharField(max_length=20)
    patient = models.CharField(max_length=20)
    link = models.CharField(max_length=20)
    doctor_id = models.CharField(max_length=20)


class HealthcareCentre(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Referral(models.Model):
    
    '''
    Model to store the information about the referral code for each workspace.
    Workspace ID (Foreign Key)| Referral Code
    '''
    referral_code = models.CharField(max_length=50, blank=True)
    healthcare_center = models.OneToOneField(HealthcareCentre, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.referral_code

    def generate_referral_code(self):
        slugified_email = slugify(self.healthcare_center.email.split("@")[0])
        hex_code = str(token_hex(2))
        slugified_hex_code = slugify(hex_code)
        referral_code = slugified_email + '-' + slugified_hex_code 
        return referral_code

    def save(self) -> None:
        referral_code = self.generate_referral_code()
        self.referral_code = referral_code

        return super().save()
    class Meta:
        verbose_name = "Referral"
        verbose_name_plural = "Referrals"
