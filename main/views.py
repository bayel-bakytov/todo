from django.shortcuts import render,HttpResponse,redirect
from .models import ToDo
from .models import Books
def homepage(request):
    return HttpResponse("hello World",)

def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"test.html",{"todo_list":todo_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)   

def books(request):
    books_list = Books.objects.all()
    return render(request,"books.html",{"books_list":books_list})    

def tester(request):
    return render(request,"tester.html")

def tester1(request):
    return render(request,"tester1.html")

def tester2(request):
    return render(request,"tester2.html")    