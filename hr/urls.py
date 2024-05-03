from django.contrib import admin
from django.urls import path,include
from hr import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('admin_login/',views.admin_login),
    path('edit/',views.edit_employee),
    path('delete/',views.delete),
    path('leave_acc/',views.leave_acc),
    path('leave_acc/accept/',views.accept_leave_acc),
    path('leave_acc/reject/',views.reject_leave_acc),
    path('add_emp',views.add_emp)
]