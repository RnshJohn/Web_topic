from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length= 39)
    phone_number = PhoneNumberField(blank=False)
    videofile = models.FileField(upload_to='images/', null=True, verbose_name="")


