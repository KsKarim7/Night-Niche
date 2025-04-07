from django.contrib import admin
from .models import UserAccount


# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['phone_no','image']


admin.site.register(UserAccount,UserAccountAdmin )
