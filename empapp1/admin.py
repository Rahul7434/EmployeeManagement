from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(EmployeeDetail)

admin.site.register(EmployeeEducation)
admin.site.register(EmployeeExperience)
