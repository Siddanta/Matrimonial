from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfileModel

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User





#admin.site.unregister(User)
admin.site.register(UserProfileModel)



