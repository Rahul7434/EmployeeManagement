from django import forms

from empapp1.models import *

class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model=EmployeeDetail
        fields = '__all__'