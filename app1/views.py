from django.shortcuts import render,redirect
from django.http import HttpResponse


def Calculator(request):
    return render(request,'calculator.html')

def Result(request):
    try:
        num1 = int(request.GET.get('number1'))
        num2 = int(request.GET.get('number2'))

    except ValueError:
        return redirect('error')
    
    
    if request.GET.get('add') == "":
            ans=num1+num2

    elif request.GET.get('substract') == "":
            ans=num1-num2

    elif request.GET.get('multiply') == "":
            ans=num1*num2

    else:
        ans=num1/num2
        
    context={
            'ans':ans
        }
    return render(request,'result.html',context)


def error(request):
      return render(request,'error.html')
