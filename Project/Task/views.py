from django.shortcuts import render,redirect
from .forms import TaskModelForm
from .models import TaskModel
# Create your views here.
def AddTask(request):
    if request.method=='POST':
        form=TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("ShowTask")
    else:
        form=TaskModelForm()
    return render(request,'task_form.html',{'form':form})

def EditTask(request,id):
    task=TaskModel.objects.get(pk=id)
    form=TaskModelForm(instance=task)
    if request.method=='POST':
        form=TaskModelForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("ShowTask")
    return render(request,'task_form.html',{'form':form})

def DeleteTask(request,id):
    task=TaskModel.objects.get(pk=id)
    task.delete()
    return redirect("ShowTask")
    



        
    