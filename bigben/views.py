from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'bigben/london.html')

def bath(request):
    return render(request,'bigben/bath.html')

def document(request):
    return render(request,'bigben/work.html')

def other(request):
    return render(request,'bigben/new.html')

def smart(request):
    return render(request,'bigben/card.html')

def java(request):
    return render(request,'bigben/js.html')

def condition(request):
    return render(request,'bigben/condition.html')

def bootstrap(request):
    return render(request,'bigben/bootstrap.html')

def array(request):
    return render(request,'bigben/array.html')

def docu(request):
    return render(request,'bigben/dom.html')

def doc(request):
    return render(request,'bigben/dom1.html')

def calcu(request):
    return render(request,'bigben/calculator.html')