from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
     return HttpResponse("hello, welcome to the basic application......")
def brian(request):
     return HttpResponse("hello, welcome to the basic application/ the brian part......")
def david(request):
     return HttpResponse("hello, <h1 style=\"color:blue\">Hello, world!</h1>")

def index(request):
     return render(request, "index.html")