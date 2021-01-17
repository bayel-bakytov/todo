from django.shortcuts import render,HttpResponse
from .models import ToDo

def homepage(request):
    return HttpResponse("hello World",)

def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"test.html",{"todo_list":todo_list})

def tester(request):
    return render(request,"tester.html")

def tester1(request):
    return render(request,"tester1.html")

def tester2(request):
    return render(request,"tester2.html")    