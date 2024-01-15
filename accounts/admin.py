from django.contrib import admin
from .models import UserModel
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_no']


admin.site.register(UserModel)