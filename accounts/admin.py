from django.contrib import admin

from accounts.models import UserData


@admin.register(UserData)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'date_joined')


# from django.contrib import admin
# from .models import UserData
#
# admin.site.register(UserData)


