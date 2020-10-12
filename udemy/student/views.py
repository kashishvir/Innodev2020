from django.shortcuts import render,redirect

# Create your views here.
def student(request):
    return render(request,'student/homepage.html')

def contact(request):
    return render(request, 'student/contact.html')