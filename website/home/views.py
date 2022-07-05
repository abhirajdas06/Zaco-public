from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from .forms import SubscibersForm




#newsletter
def subs(request):   
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')

    else:
        form = SubscibersForm()
        context = {
        'form': form,
        }
        


# Create your views here.
def index(request):
    a = subs(request)
    return render(request,"index-6.html")

def about(request):
    a = subs(request)
    return render(request,"about.html")

def contact(request): 
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['mail']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message =request.POST['message']
        if  len(name)<2 or len(email)<1 or len(phone)<10 or len(subject)<2:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, subject=subject, message=message)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
            
            
     #newsletter       
    a = subs(request)
    return render(request,"contact.html") 

def technologies(request):
    a = subs(request)
    return render(request,"technologies.html") 

