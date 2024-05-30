from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def home(request):
    data=Student.objects.all()
    return render(request,'crudApp/home.html', {'data':data})

def form(request):
     if (request.method=='POST'):
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        # reg=Student(name=name, age=age, email=email, phone_number=phone_number)
        # reg.save()

        Student.objects.create(name=name, age=age, email=email, phone_number=phone_number) #alternative method
        messages.success(request,f"Thank You {name}, Your form was Successfully Submitted")
        return redirect('home')
     return render(request,'crudApp/form.html')
def aboutus(request):
    return render(request,'crudApp/aboutus.html')
def contactus(request):
    return render(request,'crudApp/contactus.html')