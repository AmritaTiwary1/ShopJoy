from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
'''context={
    'variables':'hii'
}'''
# Create your views here.
def index(request):
    #return HttpResponse("this is my about page",context)
    return render(request,'index.html')

def about(request):
    #return HttpResponse("this is my about page")
    return render(request,'about.html')

def services(request):
    #return HttpResponse("this is my services page")
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if name=="" or email=="":
            messages.success(request,"Required fields must be filled ")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, "Your Information Has Been Submitted ! ")
         #return HttpResponse("this is my about page")
    return render(request,'contact.html')
        
        
        
    


