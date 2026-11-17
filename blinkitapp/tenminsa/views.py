from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello, world! This is the home page of the Blinkit app.")

def about(request):
    return HttpResponse("Good Morning!!! My name is Shreya. and I'm a BE Computer sceince graduate")
