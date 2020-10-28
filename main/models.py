from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    phone_number = models.CharField('Telephone', max_length= 128 ,blank=True)
    image = models.ImageField('Image', null=True, upload_to='images/', blank=True)


    class Meta:
        verbose_name = 'User profile'

    def __str__(self):
        return "{}".format(self.user.__str__())

