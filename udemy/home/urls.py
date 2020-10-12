from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.home , name = 'home'),
    path('signup',views.handleSignup, name = 'handelsignup'),
    path('login',views.handleLogin, name = 'handelelogin'),
    path('logout',views.handleLogout, name = 'handelelogout')
]