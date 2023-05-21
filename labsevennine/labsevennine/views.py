from django.shortcuts import render
from django.http import HttpResponse


def shop(request):
    return render(request, 'shop.html')

def AboutUs(request):
    return render(request, 'AboutUs.html')

def Contact(request):
    return render(request, 'Contact.html')


