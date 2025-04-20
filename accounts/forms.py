from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField  as PhoneNumberFormField
from django_countries.widgets import CountrySelectWidget


# last chatgptcode reqauired every field use 
class registration_form(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None  
        self.fields['password2'].help_text = None

        # Add HTML5 required attribute to all fields
        for field in self.fields.values():
            field.widget.attrs['required'] = 'required'

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'placeholder': 'Username',
            'required': 'required'
        }),
        help_text="Username must contain only digits or @@/*-",
        error_messages={
            'required': 'Username is required.',
            'invalid': 'Enter a valid username.'
        }
    )

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'placeholder': 'First Name',
            'required': 'required'
        }),
        error_messages={
            'required': 'First name is required.'
        }
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'placeholder': 'Last Name',
            'required': 'required'
        }),
        error_messages={
            'required': 'Last name is required.'
        }
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input-text',
            'placeholder': 'Email',
            'required': 'required'
        }),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.'
        }
    )

    country = forms.ChoiceField(
        choices=CountryField().choices,
        required=True,
        widget=CountrySelectWidget(attrs={
            'class': 'input-text country-select',
            'required': 'required'
        }),
        error_messages={
            'required': 'Please select your country.'
        }
    )

    phone_number = PhoneNumberFormField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'placeholder': 'e.g. +880123456789',
            'required': 'required'
        }),
        error_messages={
            'required': 'Phone number is required.',
            'invalid': 'Enter a valid phone number.'
        }
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'input-text',
            'placeholder': 'Password',
            'required': 'required'
        }),
        error_messages={
            'required': 'Password is required.'
        }
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'input-text',
            'placeholder': 'Confirm Password',
            'required': 'required'
        }),
        error_messages={
            'required': 'Please confirm your password.'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'phone_number', 'password1', 'password2']
   

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input-text',
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'input-text',
            'placeholder': 'Password'
        })
        self.fields['username'].error_messages.update({
            'required': 'Username is required.'
        })
        self.fields['password'].error_messages.update({
            'required': 'Password is required.'
        })
   


        