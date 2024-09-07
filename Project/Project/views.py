from django.shortcuts import render

def showtask(request):
    return render(request,'show_task.html')

def home(request):
    return render(request,'base.html')