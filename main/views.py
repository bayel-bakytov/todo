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

def add_book(request):
    form = request.POST
    text = form["todo_text"]
    todo = Books(text=text)
    todo.save()
    return redirect(books)

def delete_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request,id):
     todo = ToDo.objects.get(id=id)
     todo.is_favorite = True 
     todo.save() 
     return redirect(test)

def unmark_todo(request,id):
     todo = ToDo.objects.get(id=id)
     todo.is_favorite = False 
     todo.save() 
     return redirect(test)


