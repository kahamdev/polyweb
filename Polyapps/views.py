from django.shortcuts import render
from .models import About,Contact,Specialist

def homepage(request):
    context={}
    return render(request, 'pages/home.html', context)

def aboutpage(request):
    about=About.objects.all()
    context={
        'about':about
    }
    return render(request, 'pages/about.html', context)

def contactpage(request):
    contact=Contact.objects.all()
    context={
        'contact':contact
    }
    return render(request, 'pages/contact.html', context)

def therapypage(request):
    context={}
    return render(request, 'services/therapy.html', context)

def nursepage(request):
    context={}
    return render(request, 'services/nurse.html', context)

def specialistpage(request):
    specialist=Specialist.objects.all()
    context={
        'specialist':specialist,
    }
    return render(request, 'pages/specialist.html', context)

def servicepage(request):
    context={}
    return render(request, 'pages/service.html', context)

def inpatientpage(request):
    return render(request, 'services/inpatient.html', {})

def outpatientpage(request):
    return render(request, 'services/outpatient.html', {})
    
    
    
    
    
    
    