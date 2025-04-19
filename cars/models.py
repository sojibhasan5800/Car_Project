from django.db import models
from .constance import state_choice,door_choices,year_choice,features_choices
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from datetime import datetime
# Create your models here.

class Car(models.Model):
    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/')
    car_photo_1 = models.ImageField(upload_to='photos', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title


