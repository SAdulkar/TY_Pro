from django.contrib import admin
from django.urls import path,include
from hr import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('admin_login/',views.admin_login),
    path('edit/',views.edit_employee),
    path('delete/',views.delete),
    path('leave_acc/',views.leave_acc),
]