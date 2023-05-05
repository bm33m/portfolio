#
#@Author: Brian
#

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from profileapp.models import ProfileApp

# Create your models here.

#class SignupApp(models.Model):
#    profile_number = models.CharField(max_length=64)
#    username = models.CharField(max_length=30)


class UserApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_number = models.CharField(max_length=64)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    usertype = models.CharField(default='Other', max_length=30)
    usertypesa = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=64, blank=True)
    location = models.TextField(blank=True)
    longitude = models.CharField(max_length=128, blank=True)
    latitude = models.CharField(max_length=128, blank=True)
    address = models.TextField(blank=True)
    street = models.CharField(max_length=128, blank=True)
    town = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    province = models.CharField(max_length=128, blank=True)
    code = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=128, blank=True)
    address_type = models.CharField(default='home', max_length=30)
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(blank=True)
    date_modified = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.profile_number} {self.username} {self.address_type}"


class LoginApp(models.Model):
    profile_number = models.CharField(max_length=64)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    log_type = models.CharField(default='Signup', max_length=256)
    user_type = models.CharField(default='Other', max_length=30)
    notes = models.TextField(blank=True)
    date_login = models.DateTimeField(blank=True)
    date_logout = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.profile_number} {self.username} {self.log_type}"


class SignupForm(ModelForm):
    class Meta:
        model = ProfileApp
        fields = ['username', 'email', 'password', 'usertype']

class EditForm(ModelForm):
    class Meta:
        model = ProfileApp
        fields = ['username', 'email', 'profile_number']

class LoginForm(ModelForm):
    class Meta:
        model = ProfileApp
        fields = ['email', 'password']
