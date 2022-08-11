from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def aboutus(request):
    return render(request,'aboutus.html',{})

def homecare(request):
    return render(request,'homecare.html',{})

def donation(request):
    return render(request,'donation.html',{})

def QAlibrary(request):
    return render(request,'QAlibrary.html',{})

def li_class(request):
    return render(request,'li_class.html',{})