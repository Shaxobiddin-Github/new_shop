from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name' ,'last_name','is_staff', 'phone_number', 'photo')
    list_filter = ('is_staff', 'phone_number')
    search_fields = ('username', 'first_name', 'last_name')
    list_display_links = ('username', 'first_name', 'last_name')