from django.shortcuts import render
from django.template import Template 

# Create your views here.
def index(request):

    
    return render(request, "index.html")

def admin(request):

    return render(request, "admin.html")

def home(request):
    
    return render(request, "home.html")
    
def vice(request):
    
    return render(request, "vice.html")

def provice(request):
    
    return render(request, "provice.html")

def daf(request):
    
    return render(request, "daf.html")


def studentaff(request):
    
    return render(request, "studentaff.html")

def register(request):
    
    return render(request, "register.html")



def agric(request):
    
    return render(request, "agric.html")

def commerce(request):
    
    return render(request, "commerce.html")

def education(request):
    
    return render(request, "education.html")

def health(request):
    
    return render(request, "health.html")

def theology(request):
    
    return render(request, "theology.html")


def graduation(request):
    
    return render(request, "graduation.html")

def about(request):

    return render(request, "about.html")

def contact(request):

    return render(request, "contact.html")

def alumini(request):

    return render(request, "alumini.html")

def library(request):

    return render(request, "library.html")

def studentlib(request):

    return render(request, "studentlib.html")