from django.shortcuts import render
from .models import *
# Create your views here.
def InsertPageView(request):
    return render(request, 'insert.html')


def Insertdata(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    newuser = student.objects.create(FirstName=fname,LastName=lname, 
                                     Email=email, Contact=contact)
    
    return render(request, 'show.html')