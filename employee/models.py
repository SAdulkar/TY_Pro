from django.db import models


class Employee(models.Model):
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='SOME STRING')
    email = models.EmailField(unique=True)
    password = models.TextField(default='password')
    # phone = models.CharField(max_length=20, blank=True, null=True)
    # department = models.CharField(max_length=100)
    # position = models.CharField(max_length=100)

#add extra fields
    
class LeaveRequest(models.Model):
    """username = models.CharField(Employee, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    reason = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)"""