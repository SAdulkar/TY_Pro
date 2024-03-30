from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from employee.models import Employee  
from django.contrib import messages
from hr.models import Hr
from django.http import HttpResponse
from employee.serializers import EmployeeSerializer
# Create your views here.
def login(request):
    # cookie = request.COOKIES.get('login') 
    # print('cookie',cookie)
    # to check if user login or not
    if request.method=='POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       print(username,password)
       print(username,password)
       user = Hr.objects.filter(email=username,password=password)
       print(len(user))
       if len(user)==1:
           return redirect('/hr/admin_login')
                
    else:
            # Return an invalid login error message
        messages.error(request, 'Invalid username or password.')
    return render(request,'login.html')


def admin_login(request):
   emp = Employee.objects.all()
   context = {
       'employee':emp
   }
   return render(request,'admin_login.html',context)

def dash(request):
     employee=Employee.objects.all()
     return render(request,'admin_login.html',{'employee':employee})

def edit_employee(request):
    id = request.GET.get('id')
    print(id)
    employee = Employee.objects.filter(id=id)
    print(len(employee))
    return render(request,'edit_emp.html',{'employee':employee})
    
def delete(request):
     id = request.GET.get('id')
     employee=Employee.objects.get(id=id)
     employee.delete()
     return redirect("/hr/admin_login")