from django.shortcuts import render,redirect
from .forms import TaskCategoryForm
# Create your views here.
def AddCategory(request):
    if request.method=='POST':
        form=TaskCategoryForm(request.POST)
        if form.is_valid():
           form.save()
           print(form.cleaned_data)
    else:
        form=TaskCategoryForm()
    return render(request,"category_form.html",{'form':form}) 