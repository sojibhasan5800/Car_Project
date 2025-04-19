from django.contrib import admin
from .models import UserAddress
# Register your models here.

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'phone_number')  # Columns shown in admin list
    search_fields = ('user__first_name', 'user__email', 'phone_number')  # Search box fields
    list_filter = ('country',)  # Filter by country

