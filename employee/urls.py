from django.contrib import admin
from django.urls import path,include
from employee import views

urlpatterns = [
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('emp_dash/',views.emp_dash,name='emp_dash'),
    path('leave_req/',views.leave_req,name='leave_req'),
    path('regi/',views.regi,name='regi'),
    path('leave_req/',views.leave_req),
    
]