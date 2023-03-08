from django.shortcuts import render,redirect
from .models import *


def index(request):
    userdata = UserDetail.objects.all()
    return render(request, 'index.html', {'userdata': userdata})


def home(request):
    return render(request,'home.html')


def userDetailsAdd(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    native = request.POST.get('native')
    college = request.POST.get('college')
    CGPA = request.POST.get('CGPA')
    location = request.POST.get('location')
    UserDetail.objects.create(name=name, email=email, native=native, college=college, CGPA=CGPA, location=location).save()
    return redirect('/homeUrl')


def edituser(request, id):
    userdata = UserDetail.objects.get(id=id)
    return render(request, 'edituser.html', {'userdata': userdata})


def userDetailsUpdate(request, id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    native = request.POST.get('native')
    college = request.POST.get('college')
    CGPA = request.POST.get('CGPA')
    location = request.POST.get('location')
    UserDetail.objects.filter(id=id).update(name=name, email=email, native=native, college=college, CGPA=CGPA, location=location)
    return redirect('/')


