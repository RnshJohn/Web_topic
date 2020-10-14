from django.db import models

# Create your models here.
class userdb(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length= 39)


    def __str__(self):
        return self.name
