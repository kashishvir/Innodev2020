from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.apps import apps
Detail = apps.get_models('home','Detail')




# Create your views here.
def student(request):
    print(request.user)


    return render(request,'student/homepage.html')

def contact(request):
    return render(request, 'student/contact.html')

def grade1(request):
    return render(request, 'student/grade1.html')

def grade2(request):
    return render(request, 'student/grade2.html')

def grade3(request):
    return render(request, 'student/grade3.html')

def grade4(request):
    return render(request, 'student/grade4.html')

def grade5(request):
    return render(request, 'student/grade5.html')

def grade1sm(request):
    return render(request, 'student/grade1sm.html')

def about(request):
    return render(request, 'student/about.html')

def logout_request(request):
    logout(request)
    messages.info(request, "chala ja bhosdhike")
    return redirect("home")








