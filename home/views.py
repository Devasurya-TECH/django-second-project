from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def  about(request):
    return render(request,'contact.html')
def  booking(request):
    return render(request,'booking.html')
def  doctors(request):
    return render(request,'doctors.html')
def  contacts(request):
    return render(request,'contact.html')
def  services(request):
    return render(request,'services.html')