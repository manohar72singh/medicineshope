from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'index.html')

def registration(request):
    return render(request,'registrationform.html')

def viewMedicine(request):
    # fetch all record of medicine table

    rec = medicineRec.objects.all()
    return render(request,"viewMedicine.html",{'medicines':rec})


def viewCustomer(request):
    # fetch all records of customer table

    rec = customer.objects.all()
    return render(request,'viewCustomer.html',{'customers':rec})



def addNewCustomer(request):
    msg = ""
    if request.method=="POST":
        # create a Customer model object
        c = customer(cus_Name=request.POST['cn'],cus_Email=request.POST['em'],cus_Mob=request.POST['mob'],cus_Gen=request.POST['gen'],cus_Adds=request.POST['addr'])
        c.save()
        msg="Data Saved To Database successfully "
    f = AddNewCustomerForm()
    return render(request,"addNewCustomer.html",{'form':f,"msg":msg})


def addNewMedicine(request):
    msg = ""
    if request.method=="POST":
        c = medicineRec(medi_Name=request.POST['mn'],medi_Mfg=request.POST['mfg'],medi_Batch=request.POST['batch'],medi_Exp=request.POST['exp'],medi_Comp=request.POST['comp'],medi_Mrp=request.POST['mrp'])
        c.save()
        msg = "Data Saved To Database successfully "

    m = AddNewMedicineForm()
    return render(request,"addNewMedicine.html",{'form':m,"msg":msg})


def profile(request):
    msg = ""
    #rec = customer.objects.all()
    if request.method=="POST":
        p = Profile(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        p.save()
        msg = "Data Saved To Database successfully "
    return render(request,'registrationform.html',{'msg':msg})