from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'LoginPage2.html')

def register(request):
    return render(request,'Registration form.html')