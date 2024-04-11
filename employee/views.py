from django.shortcuts import render,HttpResponse,redirect
from employee.models import Employee
from employee.models import LeaveRequest
from employee.models import Contact
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hashlib import sha256
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

def logout(request):
   try:
      response = redirect('/')
      response.delete_cookie('login')
      response.delete_cookie('username')
      return response
   except:
      print('logout failed')
      pass
   return render(request,'index.html')

def index(request):
   cookie = request.COOKIES.get('login') 
   
   # if 'logout' in request.POST:
   #    print('loging out')
   #    response = redirect('/')
   #    response.set_cookie('login', 'false')
   #    response.set_cookie('username', None)
   #    return response
   if cookie=='true':
      try:
         emp_obj = Employee.objects.get(email = request.COOKIES.get('username'))
         context = {
         'name':emp_obj.username
         }
         return render(request,'index.html',context)

      except:
         pass
   return render(request,'index.html')

def about(request):
   return render(request,'about.html')

def contact(request):
   cookie = request.COOKIES.get('username') 
   if request.method=='POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      message = request.POST.get('message')

      try:
         conc = Contact(username=username, email=email, message=message)
         conc.save()
         return HttpResponse("Thanks for Contact US!!")
      except Exception as e:
         print(e)

   return render(request,'contact.html',{'name':cookie})

def login(request):
    # cookie = request.COOKIES.get('login') 
    # print('cookie',cookie)
    # to check if user login or not
    if request.method=='POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       print(username,password)
       emp_obj = Employee.objects.filter(email=username,password=sha256(password.encode('utf-8')).hexdigest())
       if len(emp_obj)==1:
          response = redirect('emp_dash')
          response.set_cookie('login', 'true')
          response.set_cookie('username', username)
          return response
       
       elif len(emp_obj)==0:
          
          context ={
             'msg':'Invalid Username and Password!'
          }
          return render(request,'login.html',context)
       else:
          context ={
             'msg':'Internal Server Error'
          }
          return render(request,'login.html',context)
    return render(request,'login.html')


def signup(request):
   if request.method=='POST':
      username = request.POST.get('username')
      last_name= request.POST.get('last_name')
      email = request.POST.get('email')
      password1 = request.POST.get('password1')
      password2 = request.POST.get('password2')
      print(username,password1)
      if password1==password2:
         emp_obj = Employee.objects.filter(email=email)
         if len(emp_obj)>=1:
            return render(request,'sign_up.html',{'msg':'User already exists please login!'})
         
         
         
         emp_obj =Employee(username=username,last_name=last_name,email=email,password = sha256(password1.encode('utf-8')).hexdigest())
         emp_obj.save()
         # emp_obj = Employee.objects.get(email='email')
         # emp_obj.username = 'name'
         # emp_obj.save()
         # emp = Employee.objects.filter(email='email').order_by('-id')
         # otp = 0
         # for x in emp:
         #    otp = x.otp
         #    break
         return redirect('/')
      else:
         return render(request,'sign_up.html',{'msg':'Create Password and Confirm Password doesnt match'})
   return render(request,'sign_up.html',)
# 

def regi(request):
   return render(request,'regi.html')

def emp_dash(request):
   cookie = request.COOKIES.get('username') 
   print('cookie',cookie)
   
   try:
      emp_obj = Employee.objects.get(email=cookie)
   except Exception as e:
      print(e)
   context = {
      'name':f"{emp_obj.username} {emp_obj.last_name}"
   }
   
   return render(request,'emp_dash.html',context)


def leave_req(request):
   cookie = request.COOKIES.get('username') 
   if request.method=='POST':
      start_date = request.POST.get('start_date')
      end_date = request.POST.get('end_date')
      reason = request.POST.get('reason')
      
      try:
         reque = LeaveRequest(username=cookie,leave_date_from=start_date,leave_date_to=end_date,reason=reason,leave_status=None)
         reque.save()
         return render(request, 'leave_req.html',{'msg':'Your leave request send succefully...'})
      except Exception as e:
         print(e)   
   
   return render(request, 'leave_req.html',{'name':cookie})

def leave_req_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("leave_req"))
    else:
        leave_date=request.POST.get("leave_date")
        reason=request.POST.get("reason")

        emp_obj=Employee.objects.get(admin=request.user.id)
        try:
            leave_report=LeaveRequest(username=emp_obj,leave_date=leave_date,reason=reason,leave_status=0)
            leave_report.save()
            messages.success(request, "Successfully Applied for Leave")
            return HttpResponseRedirect(reverse("emp_dash"))
        except:
            messages.error(request, "Failed To Apply for Leave")
            return HttpResponseRedirect(reverse("leave_req"))