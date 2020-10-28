# -*- coding:utf-8 _*-
""" 
@Author: John
@Email: workspace2johnwu@gmail.com
@License: Apache Licence 
@File: form.py.py 
@Created: 2020/10/18
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃            ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神獸保佑    ┣┓
                ┃　永無BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

import phonenumbers
from django import forms
from .models import *
import re
import hashlib
from PIL import Image
import io
from django.core.files.base import ContentFile

from phonenumber_field.formfields import PhoneNumberField


# class ClientForm(forms.Form):
#     phone = PhoneNumberField()


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model= UserProfile
#         fields= ["name", "imagefile"]


def email_check(email):
    pattern = re.compile("\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)




class RegisterForm(forms.Form):


    username = forms.CharField(label='username', max_length=50,
                               widget=forms.TextInput(attrs={'class': "Box-InputBox", 'id': "Box-InputBox_Registered_NickName", 'placeholder': "Username"}))
    image = forms.ImageField(label="image",
                             widget=forms.FileInput(attrs={'class': "Box-InputBox", 'id': "Box-InputBox_Registered_IDNumber"}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'Box-InputBox', 'id': 'Box-InputBox_Registered_Email', 'placeholder': 'Email'}))
    phone_number = PhoneNumberField(region='TW',widget=forms.TextInput(attrs={'class': 'Box-InputBox', 'id': 'Box-InputBox_Registered_Phone', 'placeholder': "Phone Number"}),
                               required=True)

    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': "Box-InputBox", 'id': "Box-InputBox_Registered_Password", 'placeholder': "Password"}))
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput(attrs={'class': "Box-InputBox", 'id': "Box-InputBox_Registered_RePassword", 'placeholder': "Comfirm Password"}))

    def clean_image(self):
        image = self.cleaned_data.get('image')
        md5 = hashlib.md5()
        md5.update(repr(image.name).encode('utf-8'))
        file_name = md5.hexdigest()

        if image._size > 30 * 1024 * 1024:
            raise forms.ValidationError(('File is too big.'), code='invalid')

        image = Image.open(image)


        if image.format not in ('BMP', 'PNG', 'JPEG', 'GIF'):
            raise forms.ValidationError(("Unsupported image type. Please uplod a bmp, png, jpeg, or gif."),
                                        code='invalid')
        image.thumbnail([1024, 1024], Image.ANTIALIAS)
        image_io = io.BytesIO()
        image.save(image_io, format=image.format)
        image_name = '{}.{}'.format(file_name, image.format)
        image = ContentFile(image_io.getvalue(), image_name)

        return image
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("your username must be at least 3 characters log")
        elif len(username) > 20:
            raise forms.ValidationError("your username is too long")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('your username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("your email already exists")
        else:
            raise forms.ValidationError("Please enter a valid email")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 3:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password mismatch Please enter again')

        return password2

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phonenumbers.is_valid_number(phone_number):
            raise forms.ValidationError("Number is not in TW format")
        return phone_number

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': "Box-InputBox"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "Box-InputBox"}))

    # use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if email_check(username):
            filter_result = User.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError('This emial does not exist')
        else:
            filter_result = User.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError('This username does not exist Please register first')

        return username


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    telephone = forms.CharField(label='Telephone', max_length=50, required=False)


class PwdChangeForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)

    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    # use clean methods to define custom validation rules

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch Please enter again")

        return password2