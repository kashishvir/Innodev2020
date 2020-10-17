from django.urls import path,include
from . import views

urlpatterns = [
path("logout", views.logout_request, name="logout"),

path('',views.student, name = 'student'),
path('homepage.html',views.student, name = 'student'),
path('contact.html', views.contact, name = 'student-contact'),
path('grade1.html', views.grade1, name = 'grade1'),
path('grade1sm.html', views.grade1sm, name='grade1sm'),
path('grade2.html', views.grade2, name='grade2'),
path('grade3.html', views.grade3, name='grade3'),
path('grade4.html', views.grade4, name='grade4'),
path('grade5.html', views.grade5, name='grade5'),
path('about.html',views.about, name ='about'),
path('signup.html',views.logout_request, name ='logout'),
    #path('profile.html',views.profile, name = 'profile'),


]