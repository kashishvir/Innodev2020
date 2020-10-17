from django.urls import path,include
from . import views

urlpatterns = [
    path('homepage.html' ,views.t_homepage, name='t_homepage')
]