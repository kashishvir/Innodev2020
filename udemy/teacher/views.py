from django.shortcuts import render

# Create your views here.
def t_homepage(request):
    return render(request,'teacher/homepagetr.html')
