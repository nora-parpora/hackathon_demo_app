from django.contrib import admin

from accounts.models import Profile, Employer, HouseOwner


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'date_joined')


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_joined')


@admin.register(HouseOwner)
class HouseOwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'date_joined')
