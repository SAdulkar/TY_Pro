from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from employee.models import Employee  
from django.contrib import messages
from hr.models import Hr
from django.http import HttpResponse
from employee.models import LeaveRequest
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
      
       user = Hr.objects.filter(email=username,password=password)
       print(len(user))
       if len(user)==1:
        response = redirect('/hr/admin_login')
        response.set_cookie('login', 'true')
        response.set_cookie('username', username)
        return response
        return redirect('/hr/admin_login')
                
    else:
            # Return an invalid login error message
        messages.error(request, 'Invalid username or password.')
    return render(request,'login.html')


def admin_login(request):
   emp = Employee.objects.all()
   cookie = request.COOKIES.get('username') 
   print(cookie)
   hr = Hr.objects.get(email=cookie)
   context = {
       'hr':hr.username
   }

   return render(request,'admin_login.html',context)

def dash(request):
    employee=Employee.objects.all()

    cookie = request.COOKIES.get('username') 
    print('cookie',cookie)
    try:
      emp_obj = Employee.objects.get(email=cookie)
    except Exception as e:
      print(e)
    context = {
      'name':f"{emp_obj.username}"
   }
    
    return render(request,'admin_login.html',{'employee':employee}, context)

def edit_employee(request):
    id = request.GET.get('id')
    print(id)
    employee = Employee.objects.filter(id=id)
    if request.method == 'POST':
        print('updating ')
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        department = request.POST.get('department')
        position = request.POST.get('position')
        salary = request.POST.get('salary')
        hired_date = request.POST.get('hired_date')
        print(department)

        employee = Employee.objects.get(id=id)
        employee.username = username
        employee.last_name=last_name
        employee.email = email
        
        employee.phone_number = phone_number
        employee.date_of_birth = date_of_birth
        employee.address = address
        employee.department = department
        employee.salary = salary
        employee.hired_date = hired_date
        employee.position = position
        employee.save()

        return redirect('/hr/admin_login')     
    return render(request,'edit_emp.html',{'employee':employee})
    
def delete(request):
     id = request.GET.get('id')
     employee=Employee.objects.get(id=id)
     employee.delete()
     return redirect("/hr/admin_login")

def leave_acc(request):      
   leave = LeaveRequest.objects.filter(leave_status=None)
   return render(request,'leave_acc.html', {'leave':leave})

def accept_leave_acc(request):
   id = request.GET.get('id')      
   leave = LeaveRequest.objects.get(id=id)
   leave.leave_status = 'Accepted'
   leave.save()
   return redirect('/hr/leave_acc')



def add_emp(request):
   if request.method == 'POST':
        # Retrieve form data from POST request
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        department = request.POST.get('department')
        position = request.POST.get('position')
        salary = request.POST.get('salary')
        hired_date = request.POST.get('hired_date')
        
        # Create Employee object and save to database
        employee = Employee(
            username=username,
            last_name=last_name,
            email=email,
            password=password,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            address=address,
            department=department,
            position=position,
            salary=salary,
            hired_date=hired_date
        )
        employee.save()
   return render(request,'emp_add.html')


def reject_leave_acc(request):
   id = request.GET.get('id')      
   leave = LeaveRequest.objects.get(id=id)
   leave.leave_status = 'Rejected'
   leave.save()
   return redirect('/hr/leave_acc')

def leavepending(request):
    leave = LeaveRequest.objects.all().order_by('-id')
    return render(request,'leavepending.html',{'leave':leave})  

def update_status(request):
    
    pass

