from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request,'login.html')
    
def home(request):
    return render(request,'index.html')

def addBeneficiary(request):
    return render(request,'addben.html')

def settings(request):
    return render(request,'settings.html')

def transactions(request):
    return render(request, 'transactions.html')
