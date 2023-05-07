from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()
# Register your models here.
@admin.register(User) #use the UserAdmin class to edit User objects in the admin site
class UserAdmin(UserAdmin):
    pass