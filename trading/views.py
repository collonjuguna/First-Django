from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home page.html')

def warehouse(request):
    return render(request,'warehouse.html')

def payment(request):
    return render(request,'payment.html')

def HOME(request):
    return render(request,'HOME.html')

def about(request):
    return render(request,'about.html')

def form(request):
    return render(request,'Form.html')
