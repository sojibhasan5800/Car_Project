from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from .forms import registration_form,CustomLoginForm
from .models import UserAddress
from contacts.models import Contact 

# Create your views here.

def register(request):


    # Approach->1
    # if request.method == 'POST':
    #     firstname = request.POST['firstname']
    #     lastname = request.POST['lastname']
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']

        # Approach->2
    if request.method == 'POST':
        register_form = registration_form(request.POST)
        
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password1']
            confirm_password = register_form.cleaned_data['password2']
            country = register_form.cleaned_data['country']
            phone_number = register_form.cleaned_data['phone_number']
        

            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists!')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Email already exists!')
                        return redirect('register')
                    else:
                        our_user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                        UserAddress.objects.create(
                            user = our_user,
                            country = country,
                            phone_number = phone_number
                        )
                        auth.login(request, our_user)
                        messages.success(request, 'You are now logged in.')
                        return redirect('dashboard')
                        
        else:
            messages.error(request, 'Password do not match')
            return render(request, 'accounts/register.html',{'form':register_form})
    else:
        register_form = registration_form()
        return render(request, 'accounts/register.html',{'form':register_form})
    
def login(request):
    if request.method == 'POST':
        login_form = CustomLoginForm(request,data =request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        login_form = CustomLoginForm()
        
    return render(request, 'accounts/login.html',{'form':login_form})



def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id = request.user.id)
    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html',data)


@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

    


    

