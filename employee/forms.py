from django import forms
from employee.models import Employee  
from .models import LeaveRequest

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['username', 'last_name', 'email'] 
        widgets = { 'username': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'last_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
      }

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['emp_id', 'leave_date', 'leave_message', 'leave_status']
