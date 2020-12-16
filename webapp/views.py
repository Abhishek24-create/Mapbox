from django.shortcuts import render,redirect
# from django.views.generic import TemplateView, ListView
# from django.contrib import messages
from webapp.models import  register
from django.http import HttpResponseRedirect
# from django.contrib.sessions.models import Session
# from datetime import datetime
# Create your views here.
# Create your views here.
def Registration(request):
    return render(request,'MyApp/registration.html')

def SaveRegister(request):
    firstname = request.POST.get("firstname")
    email = request.POST.get("email")
    mob = request.POST.get("phone no")
    password = request.POST.get("password")
    auth=register.objects.filter(email=email).count()
    if auth>0:
        message="User Already Registered With This User"
        return render(request, "MyApp/registration.html", {'message': message})
    else:
        register(firstname=firstname, email=email, mob=mob, password=password).save()
    return render(request, "MyApp/login.html")

def Login(request):

    if request.POST:
        email= request.POST.get('email')
        password = request.POST.get('password')
        count = register.objects.filter(email=email,password=password)
        if count.count()>0:
            request.session['useremail'] = email
            return redirect("/", {'useremail':email})
        else:
            return render(request,"MyApp/login.html",{'message':'Invalid User or Password'})


def mapbox(request):
    return render(request, 'MyApp/mapbox.html'),


def aap(request):
    return render(request, 'MyApp/aap.html'),
