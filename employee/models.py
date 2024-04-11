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
    
class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    message=models.TextField()

    
class LeaveRequest(models.Model):
    username = models.CharField(max_length=100)
    leave_date_from = models.DateField()
    leave_date_to = models.DateField()
    reason = models.TextField()
    leave_status = models.CharField(max_length=10,default=None,blank=True,null=True)
    