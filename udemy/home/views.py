from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt




from .models import Detail
grade = ""
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    #return HttpResponse("this is shit")


def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        grade = request.POST['grade']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        detail = Detail(username=username,grade=grade, fname = fname, lname = lname)
        detail.save()

        if not username.isalnum():
            messages.error(request,'username should only contain lettrs and numbers')
            return redirect('home')
        if len(username) > 10:
            messages.error(request, 'username is very long')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "password do not match")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)


        myuser.save()


        email_subject= 'ERUDITION TEAM'
        email_body = 'your account has been registered to erudition'
        send_mail(
                email_subject,
                email_body,
              "testuser@gmail.com",
              [email],
        )

        #messages.success(request,'your account has been created')
        return redirect('home')


    else:
        return HttpResponse("not allowed")

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username = loginusername, password = loginpassword)


        if user is not None:
            #c = Detail.objects.get(username = loginusername)
            c=''
            login(request, user)
            messages.success(request, ' successfully logged in')
            return render(request,'student/homepage.html',{'c':c})
        else:
            messages.error(request, 'Invalid credentials : PLEASE TRY AGAIN')
            return redirect('home')
    else:
        return HttpResponse("404-error found")



def handleLogout(request):
    logout(request)
    messages.success(request,'chale ja bhosdhike')
    return redirect('home')

