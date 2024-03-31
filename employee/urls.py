from django.contrib import admin
from django.urls import path,include
from employee import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('regi/',views.regi,name='regi'),
    path('dash/',views.dash,name='dash'),
    path('delete/<int:id>',views.delete, name='delete'),
]