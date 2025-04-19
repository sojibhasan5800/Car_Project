from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='user_address', on_delete=models.CASCADE)
    country =CountryField(blank_label='(select country)')
    phone_number = PhoneNumberField(region=None)

    def __str__(self):
        return str(self.user.first_name)
