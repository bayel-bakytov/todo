from django.shortcuts import render,HttpResponse


def homepage(request):
    return HttpResponse("hello World")

def test(request):
    return render(request,"test.html")

def go(request):
    return HttpResponse("This is my first page.")    


def fizz_buzz(request,a=15): 
    if a % 3 == 0 and a % 5 == 0:
       return HttpResponse("«FizzBuzz»")
    elif a % 5 == 0:
        return HttpResponse("<<Buzz>>")
    elif a % 3 == 0:
        return HttpResponse("«Fizz»")  
    else:
        return a     

    