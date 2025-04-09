from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField  as PhoneNumberFormField
from django_countries.widgets import CountrySelectWidget



class registration_form(UserCreationForm):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None  
        self.fields['password2'].help_text = None
        
    country = forms.ChoiceField(
        choices=CountryField().choices,
        required=True,
        widget=CountrySelectWidget(attrs={'class': 'form-controls'}),
        error_messages={'required': 'Please select your country.'}
    )
    phone_number = PhoneNumberFormField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-controls', 'placeholder': 'e.g. +880123456789'}),
        error_messages={'required': 'Phone number is required.'}
    )


    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-controls'}) 
                             ,error_messages={'required': "Emails is required.", 'invalid': "Enter a valid email address."})   
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-controls'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','country','phone_number']
        labels={
            'username':'user_Name',
        }
        help_texts={
            'username':'usernameMust Be fields @@/*-',  
        }
   


        