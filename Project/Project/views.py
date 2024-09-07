from django.shortcuts import render
from Category.models import TaskCategoryModel
from Task.models import TaskModel
def showtask(request):
    TaskList=TaskModel.objects.all()
    return render(request,'show_task.html',{'TaskList':TaskList})

def home(request):
    return render(request,'base.html')