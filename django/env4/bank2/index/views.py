from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserAccount, bankdetails, AddBen
import random

# Create your views here.
def entry(request):
    banks = bankdetails.objects.all()
    data = {'bankdetails': banks}
    if request.POST:
        fname       = request.POST.get('fname')
        lname       = request.POST.get('lname')
        username    = request.POST.get('username')
        email       = request.POST.get('email')
        password    = request.POST.get('password')
        user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email, password= password)
        user.save()
        dob         = request.POST.get('dob')
        phone       = request.POST.get('phone')
        address     = request.POST.get('address')
        bank        = request.POST.get('bank')
        branch      = request.POST.get('branch')
        UserAccount.objects.create(user_id= user.id,dob=dob, phone=phone, address=address, bank=bank, branch= branch)
        # print(f_name,l_name,phone,email,dob,address,select)
        # return redirect(log_in)
        return redirect(login_user)
    return render(request,'signup.html',data)

def login_user(request):
    if request.POST:
        username = request.POST.get('username',False)
        password = request.POST.get('password',False) 
        user = authenticate(username= username,password= password)
        if user is not None:
            login(request,user)
            return redirect(summary)
        else:
            return redirect(entry)
    return render(request,'login.html')

def summary(request):
    if request.user.is_authenticated:
        userinfo = UserAccount.objects.get(user_id= request.user.id)
        data = {'UserAccount': userinfo}
        # print(data)
    else:
        return redirect(login_user)
    return render(request,'summary.html',data)

def logout_user(request):
    logout(request)
    return redirect(login_user)

def addben(request):
    if request.user.is_authenticated:
        if request.POST:
            # userinfo = UserAccount.objects.get(user_id= request.user.id)
            ben_acc  =   request.POST.get('ben_acc')
            ben_reacc  =   request.POST.get('ben_reacc')
            ben_ifsc=   request.POST.get('ben_ifsc')
            ben_name=   request.POST.get('ben_name')
            if (ben_acc == ben_reacc):
                AddBen.objects.create(user_id= request.user.id, beneficiary_accno=ben_acc, ifsc_code=ben_ifsc,beneficiary_name=ben_name)
            else:
                return redirect(addben)
    else:
        return redirect(entry)
    return render(request,'addben.html')

def transfer(request):
    return render(request,'transfer.html')

def transactions(request):
    return render(request,'transactions.html')

def settings(request):
    return render(request,'settings.html')