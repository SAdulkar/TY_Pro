from django.db import models


class Employee(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, default='SOME STRING', null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.TextField(default='password', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hired_date = models.DateField(null=True, blank=True)

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
    