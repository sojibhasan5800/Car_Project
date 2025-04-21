from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
import json
import os
from django.conf import settings
from django.utils.dateparse import parse_datetime

# Create your views here.

def home(request):
    json_path = os.path.join(settings.BASE_DIR,'cars_api.json')
    with open(json_path,'r',encoding='utf-8') as file:
        data = json.load(file)
    
    for item in data:
        fields = item['fields']
        vin_no = fields.get('vin_no')

        if not Car.objects.filter(vin_no=vin_no).exists():
            if 'features' in fields:
                fields['features'] = [f.strip() for f in fields['features'].split(',')]
            
            if 'created_date' in fields:
                fields['created_date'] = parse_datetime(fields['created_date'])
            try:
                Car.objects.create(**fields)  # নতুন গাড়ি সেভ করা
                print(f"✅ Saved: {fields['car_title']}")
            except Exception as e:
                print(f"❌ Error saving car: {e}")
        else:
            print(f"❌ Car with VIN {vin_no} already exists!")


    

        
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)

def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from CarDealer Website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'rathan.kumar049@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)
