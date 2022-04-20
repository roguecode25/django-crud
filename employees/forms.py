from dataclasses import field, fields
from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'Employee Code',
            'gender': 'Gender',
            'base_pay': 'Base Salary',
            'bonus' : 'Bonus Pay'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
    