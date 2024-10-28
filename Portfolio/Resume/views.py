
from django.shortcuts import render
# Create your views here.
def Home(r):
    return render(r,'home.html')
def About(r):
    return render(r,'about.html')
def Resume(r):
    return render(r,'resume.html')
def Contact(r):
    return render(r,'contact.html')
def Project(r):
    return render(r,'project.html')
def Project1(r):
    return render(r,'project1.html')
def Education(r):
    return render(r,'education.html')
def Skills(r):
    return render(r,'skills.html')