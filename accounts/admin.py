from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'age' , 'is_staff', 'is_active' , 'date_joined' ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}), 
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, { 'fields': ('age',) } ),
    )

admin.site.register(CustomUser, CustomUserAdmin)