from django.shortcuts import render, redirect
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
    
    return redirect("showpage")



def ShowPage(request):

    all_data = student.objects.all()
    print(all_data)
    return render(request, 'show.html', {'key1': all_data})





def EditPage(request, pk):
    get_data=student.objects.get(id=pk)
    return render(request, 'edit.html', {'key2': get_data})


def UpdateData(request, pk):
    udata = student.objects.get(id=pk)
    udata.FirstName = request.POST['fname']
    udata.LastName = request.POST['lname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']

    udata.save()
    return redirect('showpage')


def DeleteData(request, pk):
    udata=student.objects.get(id=pk)
    udata.delete()
    return redirect('showpage')


def filterView(request):
    pk=request.POST['filId']
    fname=request.POST['filFname']
    lname=request.POST['filLname']
    email=request.POST['filEmail']
    contact=request.POST['filContact']


    get_data=student.objects.filter(id=pk).values()
    
    return render(request, 'filtershow.html', {'key3': get_data})
    