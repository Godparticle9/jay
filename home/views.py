import email
from django.shortcuts import render, HttpResponse
from home.models import Contact



# Create your views here.
def home(request):
    context={'name':'jayant','empid':'15654'}
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        phone=request.POST['phone']
        print(name,email,address,city,phone)
        ins=Contact(name=name,email=email,phone=phone,address=address,city=city)
        ins.save()
        print('data has been written to the db')

    return render(request,'contact.html')

