from django.contrib import admin

# Register your models here.
from users.models import CustomUser, TimeClock

admin.site.register(CustomUser)
admin.site.register(TimeClock)
