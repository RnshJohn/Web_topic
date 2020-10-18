from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField


# class ClientForm(forms.Form):
#     phone = PhoneNumberField()



class ImageForm(forms.ModelForm):
    class Meta:
        model= Client
        fields= ["name", "imagefile"]