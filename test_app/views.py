from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(req):
  return HttpResponse("This is course page")

def about(req):
  return HttpResponse("This is course about page")