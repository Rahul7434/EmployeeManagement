from django import forms
from .models import *

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = EmployeeExperience
        fields = '__all__'

class EmployeeEducationForm(forms.ModelForm):
    class Meta:
        model= EmployeeEducation
        fields = '__all__'


