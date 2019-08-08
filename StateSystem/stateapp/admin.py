from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import State, Attendance, Table

admin.site.register(State)
admin.site.register(Attendance)
admin.site.register(Table)
