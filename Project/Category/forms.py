from .models import TaskCategoryModel
from django import forms

class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model=TaskCategoryModel
        fields='__all__'

