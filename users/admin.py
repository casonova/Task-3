
from django.contrib import admin

from .models import User


@admin.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display=['email','username','name','password','created_date','updated_date']
    search_fields=['email']
