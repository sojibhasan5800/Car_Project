from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from .forms import registration_form
from .models import UserAddress

# Create your views here.

def register(request):

    if request.method == 'POST':
        register_form = registration_form(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password1']
            confirm_password = register_form.cleaned_data['password2']
            country = register_form.changed_data['country']
            phone_number = register_form.changed_data['phone_number']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    # user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)

                    our_user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    UserAddress.objects.create(
                        user = our_user,
                        country = country,
                        phone_number = phone_number
                    )
                    auth.login(request, our_user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
